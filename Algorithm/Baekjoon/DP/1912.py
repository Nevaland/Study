import sys

n = int(sys.stdin.readline())
table = list(map(int, sys.stdin.readline().split()))
dp_mem = [0] * n
dp_mem[0] = table[0]

for i in range(1, n):
    if dp_mem[i-1] < 0:
        dp_mem[i] = table[i]
    else:
        dp_mem[i] = dp_mem[i-1] + table[i]

print(max(dp_mem))
