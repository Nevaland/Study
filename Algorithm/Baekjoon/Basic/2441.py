import sys

n = int(sys.stdin.readline())

for i in range(n):
    print(' ' * i + '*' * (n-i))