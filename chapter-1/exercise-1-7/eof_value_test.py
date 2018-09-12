from sys import argv, exit, stderr
from subprocess import run, PIPE

INPUT = 'a'
EXPECTED = '''-1
'''

executable_path = argv[1]
completed_process = run([executable_path],
    input=INPUT,
    stdout=PIPE,
    encoding='utf8',
    universal_newlines=True)

output = completed_process.stdout
if output != EXPECTED:
    print("Output differs from expected.", file=stderr)
    exit(1)

exit(0)
