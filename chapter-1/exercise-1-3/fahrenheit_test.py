from sys import argv, exit, stderr
from subprocess import run, PIPE

EXPECTED = '''  F      C
  0  -17.8
 20   -6.7
 40    4.4
 60   15.6
 80   26.7
100   37.8
120   48.9
140   60.0
160   71.1
180   82.2
200   93.3
220  104.4
240  115.6
260  126.7
280  137.8
300  148.9
'''

executable_path = argv[1]
completed_process = run([executable_path], stdout=PIPE)

output = completed_process.stdout.decode('utf8')
if output != EXPECTED:
    print("Output differs from expected.", file=stderr)
    exit(1)

exit(0)
