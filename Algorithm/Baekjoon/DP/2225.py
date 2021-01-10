# D[N][K] = D[N-j][K-1]
import sys

n, k = map(int, sys.stdin.readline().split())
dp_mem = [[0]*(k+1) for _ in range(n+1)]

for ki in range(1, k+1):
    for ni in range(1, n+1):
        if ki == 1:
            dp_mem[ni][ki] = 1
        else:
            for j in range(0, ni):
                dp_mem[ni][ki] += dp_mem[ni-j][ki-1]
            dp_mem[ni][ki] += 1 

print(dp_mem[n][k] % 1000000000)
