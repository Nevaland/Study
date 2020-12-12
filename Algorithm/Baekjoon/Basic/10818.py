import sys

sys.stdin.readline()
values = list(map(int, sys.stdin.readline().split()))

print("%d %d" % (min(values), max(values)))