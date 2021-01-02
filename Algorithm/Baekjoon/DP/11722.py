import sys

n = int(sys.stdin.readline())
table = list(map(int, sys.stdin.readline().split()))
dp_mem = [0] * n

for i in range(n):
    for j in range(i):
        if table[j] > table[i]:
            dp_mem[i] = max(dp_mem[i], dp_mem[j] + 1)
    if dp_mem[i] == 0:
        dp_mem[i] = 1

print(max(dp_mem))
