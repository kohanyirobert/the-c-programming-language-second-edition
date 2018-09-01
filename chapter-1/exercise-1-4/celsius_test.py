from sys import argv, exit, stderr
from subprocess import run, PIPE

EXPECTED = '''  C      F
  0   32.0
 20   68.0
 40  104.0
 60  140.0
 80  176.0
100  212.0
120  248.0
140  284.0
160  320.0
180  356.0
200  392.0
220  428.0
240  464.0
260  500.0
280  536.0
300  572.0
'''

executable_path = argv[1]
completed_process = run([executable_path], stdout=PIPE)

output = completed_process.stdout.decode('utf8')
if output != EXPECTED:
    print("Output differs from expected.", file=stderr)
    exit(1)

exit(0)
