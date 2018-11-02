from sys import argv, exit, stderr
from subprocess import run, PIPE

EXECUTABLE_PATH = argv[1]

def assert_output(actual_input, expected_output):
    completed_process = run([EXECUTABLE_PATH],
        input=actual_input,
        stdout=PIPE,
        encoding='utf8',
        universal_newlines=True)

    actual_output = completed_process.stdout
    if actual_output != expected_output:
        print('Output differs: actual {}, expected: {}', output, expected_output, file=stderr)
        exit(1)

    exit(0)

assert_output('', '')
assert_output('a', 'a')
assert_output('aa', 'aa')
assert_output('a a', 'a a')
assert_output('a\ta', 'a\\ta')
assert_output('a\ba', 'a\\bta')
assert_output('a\\a', 'a\\\\ta')
assert_output('a\t\b\\a', 'a\\t\\b\\\\ta')
