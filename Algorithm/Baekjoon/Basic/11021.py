import sys

for i in range(int(sys.stdin.readline())):
    print("Case #" + str(i + 1), end=": ")
    print(sum(map(int, sys.stdin.readline().split())))