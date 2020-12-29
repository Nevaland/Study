# D(n) = D(n-1) + D(n-2)
import sys

n = int(sys.stdin.readline())
dp_mem = [0]*(n+1)

def dp(x):
    if x == 1: return 1
    if x == 2: return 2
    if not dp_mem[x]: 
        dp_mem[x] = dp(x-1) + dp(x-2)
    return dp_mem[x]

sys.setrecursionlimit(2000)
print(dp(n) % 100007)