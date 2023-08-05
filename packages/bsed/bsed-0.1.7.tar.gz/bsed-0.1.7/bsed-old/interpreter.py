import sys
from os import path
import subprocess
from .token_tree import TokenTree
import bsed.definitions as definitions
from .arg_process import process_args


class Interpreter:
    accepted_flags = {'-i', '-t'}

    def __init__(self, command_tree_file, translations_file, line_condition_tree_file,
                 line_condition_translations_file):
        self.command_tree = TokenTree.from_json(command_tree_file, translations_file)
        self.line_condition_tree = TokenTree.from_json(line_condition_tree_file, line_condition_translations_file)

    def print_commands(self):
        print("Supported commands:", file=sys.stderr)
        for k in self.command_tree.command_translations:
            print(' >', k, file=sys.stderr)

    def build_command(self, command_args, file_arg) -> (str, [str]):
        if file_arg is None:
            file_arg = ''
        cmd_statement, flags = process_args(command_args)
        unsupported_flags = [f for f in flags if f not in Interpreter.accepted_flags]
        if len(unsupported_flags) > 0:
            print('Invalid flags:', unsupported_flags, file=sys.stderr)
            return None, None

        # tree.print_command_tree()
        line_condition, line_condition_user_text_inputs, num_line_condition_words = \
            self.line_condition_tree.validate_command(
            cmd_statement)
        cmd, user_text_inputs, num_cmd_words = self.command_tree.validate_command(cmd_statement[num_line_condition_words:])
        print(num_cmd_words)
        if cmd is None or num_line_condition_words + num_cmd_words != len(cmd_statement):
            return None, None
        args = [file_arg] + user_text_inputs
        cmd = cmd.format(*args)
        return cmd, flags

    @classmethod
    def execute_command(cls, cmd, flags, return_output=False, stdin=sys.stdin):
        if cmd is None:
            return None
        res = None
        translation_only = '-t' in flags
        in_place = '-i' in flags
        if in_place:
            parts = cmd.split()
            cmd = ' '.join(parts[:-1] + ['-i'] + [parts[-1]])
        if translation_only:
            print('Translation:\n >', cmd)
        else:
            # if return_output:
            #     with popen(cmd) as fout:
            #         return fout.read()
            stdout = subprocess.PIPE if return_output else None
            with subprocess.Popen(cmd, shell=True, stdout=stdout, stdin=stdin) as p:
                try:
                    # exit_code = subprocess.call(cmd, shell=True, stdout=stdout)
                    exit_code = p.wait()
                    if exit_code < 0:
                        print("Child was terminated by signal", -exit_code, file=sys.stderr)
                except OSError as e:
                    print("Execution failed:", e, file=sys.stderr)
                if return_output:
                    res = bytes.decode(p.stdout.read())
        return res


def default_interpreter():
    command_tree_fp = definitions.COMMAND_TOKEN_TREE_FILE
    translations_fp = definitions.COMMAND_TRANSLATIONS_FILE
    filter_tree_fp = definitions.LINE_CONDITION_TOKEN_TREE_FILE
    filter_tranlations_fp = definitions.LINE_CONDITION_TRANSLATIONS_FILE
    return Interpreter(command_tree_fp, translations_fp, filter_tree_fp, filter_tranlations_fp)


def print_commands():
    default_interpreter().print_commands()


def main():
    if len(sys.argv) < 2:
        print('Insufficient arguments. Format: \'bsed <input-file> <command statement>\'\n'
              'Examples: \n'
              '> bsed example.txt delete lines starting with "example Phrase"\n'
              '> bsed example.txt select lines containing Andrew\n'
              '> bsed example.txt prepend beat with "Don\'t stop the "', file=sys.stderr)
        exit(1)

    # std_in = None
    # if sys.stdin is not None:
    #     file_arg = None
    #     command_args = sys.argv[1:]
    #     std_in = sys.stdin
    file_arg = None
    if path.exists(sys.argv[1]):
        file_arg = sys.argv[1]
        command_args = sys.argv[2:]
    elif path.exists(sys.argv[-1]):
        file_arg = sys.argv[-1]
        command_args = sys.argv[1:-1]
    else:
        # print('File not found. Reading from standard input.', file=sys.stderr)
        command_args = sys.argv[1:]

    interpreter = default_interpreter()
    cmd, flags = interpreter.build_command(command_args, file_arg)
    if cmd is not None:
        interpreter.execute_command(cmd, flags)
    else:
        print('Invalid command.', file=sys.stderr)
