import sys

n = int(sys.stdin.readline())

for i in range(n-1):
    print(' ' * (n-1-i) + '*' + (' ' * (i*2-1)) + ('*' if i != 0 else ''))
print('*' * (n*2-1))
