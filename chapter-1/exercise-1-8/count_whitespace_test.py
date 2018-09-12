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

assert_output('', '''Blanks: 0
Tabs: 0
Newlines: 0
''')

assert_output('Lorem ipsum dolor sit amet.', '''Blanks: 4
Tabs: 0
Newlines: 0
''')

assert_output('Lorem\tipsum\tdolor\tsit\tamet.', '''Blanks: 0
Tabs: 4
Newlines: 0
''')

assert_output('Lorem\nipsum\ndolor\nsit\namet.', '''Blanks: 0
Tabs: 0
Newlines: 4
''')

assert_output('Lorem\tipsum dolor\tsit\namet.\n', '''Blanks: 1
Tabs: 2
Newlines: 2
''')
