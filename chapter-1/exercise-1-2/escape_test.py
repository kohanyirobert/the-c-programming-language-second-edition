from sys import argv, exit
from subprocess import run, PIPE

executable_path = argv[1]
run([executable_path], stdout=PIPE, encoding='utf8', universal_newlines=True)

exit(0)
