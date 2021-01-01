# 10 30 31 12 14 30 31
#  1  2  3  2  3  4  5
#  0  1  2  3
import sys

n = int(sys.stdin.readline())
table = list(map(int, sys.stdin.readline().split()))
dp_mem = [0] * n

for i in range(n):
    for j in range(i):
        if table[j] < table[i]:
            dp_mem[i] = max(dp_mem[i], dp_mem[j] + 1)
    if dp_mem[i] == 0:
        dp_mem[i] = 1

print(max(dp_mem))
