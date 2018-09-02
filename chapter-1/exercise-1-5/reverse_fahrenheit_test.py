from sys import argv, exit, stderr
from subprocess import run, PIPE

EXPECTED = '''  F      C
300  148.9
280  137.8
260  126.7
240  115.6
220  104.4
200   93.3
180   82.2
160   71.1
140   60.0
120   48.9
100   37.8
 80   26.7
 60   15.6
 40    4.4
 20   -6.7
  0  -17.8
'''

executable_path = argv[1]
completed_process = run([executable_path], stdout=PIPE, encoding='utf8', universal_newlines=True)

output = completed_process.stdout
if output != EXPECTED:
    print("Output differs from expected.", file=stderr)
    exit(1)

exit(0)
