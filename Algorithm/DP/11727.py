# 1:1, 2:3, 3:5 ..
# # D(n) = D(n-1) + 2*D(n-2)
import sys

n = int(sys.stdin.readline())
dp_mem = [0]*(n+1)
dp_mem[1] = 1

if n != 1:
    dp_mem[2] = 3
    for i in range(3, n+1):
        dp_mem[i] = dp_mem[i-1] + 2 * dp_mem[i-2]

print(dp_mem[n] % 10007)