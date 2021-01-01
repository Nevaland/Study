# d(n) = 2*d(n-1) - (n-1)
import sys

n = int(sys.stdin.readline())
dp_mem = [[0]*10 for _ in range(n+1)]
for i in range(1, 10):
    dp_mem[1][i] = 1
    
for i in range(2, n+1):
    dp_mem[i][0] = dp_mem[i-1][1]
    dp_mem[i][9] = dp_mem[i-1][8]
    for j in range(1,9):
        dp_mem[i][j] = dp_mem[i-1][j-1] + dp_mem[i-1][j+1]
    
print(sum(dp_mem[n]) % 1000000000)
