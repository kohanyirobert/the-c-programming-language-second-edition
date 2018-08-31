from sys import argv, exit, stderr
from subprocess import run, PIPE

executable_path = argv[1]
completed_process = run([executable_path], stdout=PIPE)

output = completed_process.stdout.decode('utf8')
if output != 'hello, world\n':
    print("Expected newline character at the of the output.", file=stderr)
    exit(1)

exit(0)
