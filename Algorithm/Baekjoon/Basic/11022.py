import sys

for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d" % (i+1, a, b, a+b))
