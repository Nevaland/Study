import sys

for line in sys.stdin:
    result = sum(map(int, line.split()))
    if result == 0:
        break
    print(result)