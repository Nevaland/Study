# d[n] = max(d[n-1], d[n-2]+table[n], d[n-3]+table[n-1]+table[n])
import sys

n = int(sys.stdin.readline())
table = [0] + [int(sys.stdin.readline()) for _ in range(n)]
dp_mem = [0] * (n+1)

dp_mem[1] = table[1]
if 1 < n:
    dp_mem[2] = table[1] + table[2]
for i in range(3, n+1):
    dp_mem[i] = max(dp_mem[i-1], 
                    dp_mem[i-2] + table[i], 
                    dp_mem[i-3] + table[i-1] + table[i])

print(dp_mem[n])
