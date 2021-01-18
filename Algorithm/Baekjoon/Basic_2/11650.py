import sys

coordinates = list()
n = int(sys.stdin.readline())
for _ in range(n):
    coordinates.append(tuple(map(int, sys.stdin.readline().split())))
coordinates.sort()

print('\n'.join(map(lambda x: str(x[0]) + ' ' + str(x[1]), coordinates)))
