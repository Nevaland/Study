# D[n] = max(D[n-2]+T[n], D[n-3]+T[n-1]+T[n])
import sys

n = int(sys.stdin.readline())
table = [int(sys.stdin.readline()) for _ in range(n)]
dp_mem = table[:]

for i in range(n):
    if 0 < i:
        dp_mem[i] = table[i-1] + table[i]
    if 1 < i:
        dp_mem[i] = max(dp_mem[i-2]+table[i], dp_mem[i])
    if 2 < i:
        dp_mem[i] = max(dp_mem[i-3]+table[i-1]+table[i], dp_mem[i])

print(dp_mem[-1])
