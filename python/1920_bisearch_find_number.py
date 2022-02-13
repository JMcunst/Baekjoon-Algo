from sys import stdin, stdout

num_n = stdin.readline()
N = set(stdin.readline().split())
num_m = stdin.readline()
M = stdin.readline().split()

for l in M:
    stdout.write('1\n') if l in N else stdout.write('0\n')