import sys, math

unit = 10
line = sys.stdin.readline()
for i in range(math.ceil(len(line) / unit)):
    print(line[unit*i: unit*(i + 1)])