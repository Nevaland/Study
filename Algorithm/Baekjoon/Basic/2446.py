import sys

n = int(sys.stdin.readline())

for i in range(n-1, 0, -1):
    print(' ' * (n-1-i) + ('*' * (i*2+1)))
for i in range(n):
    print(' ' * (n-1-i) + ('*' * (i*2+1)))
