import sys

n = int(sys.stdin.readline())

for i in range(n):
    print(' ' * (n-1-i) + ('*' * (i+1)))
for i in range(1, n):
    print(' ' * i + '*' * (n-i))
