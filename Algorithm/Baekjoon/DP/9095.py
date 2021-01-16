# d(n) = d(n-1) + d(n-2) + d(n-3)
import sys

T = int(sys.stdin.readline())
dp_mem = [0,1,2,4]

for _ in range(T):
    n = int(sys.stdin.readline())
    origin_len = len(dp_mem)
    if n >= origin_len:
        dp_mem.extend([0]*(n-origin_len+1))
        for i in range(origin_len, n+1):
            dp_mem[i] = dp_mem[i-1] + dp_mem[i-2] + dp_mem[i-3]
    print(dp_mem[n])
