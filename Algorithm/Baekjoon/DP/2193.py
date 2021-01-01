# 1 - 1 =(0,1)
# 2 - 10 =(1,0)
# 3 - 100, 101 (1,1)
# 4 - 1000, 1001, 1010 (2,1)
# 5 - 10000,10001, 10010, 10100,10101 (3,2)
# 6 - ([3]+[2], [3])
# d[n][0] = d[n-1][0] + d[n-1][1]
# d[n][1] = d[n-1][0]
import sys

n = int(sys.stdin.readline())
dp_mem = [[0]*2 for _ in range(n+1)]
dp_mem[1] = [0,1]

for i in range(2, n+1):
    dp_mem[i][0] = dp_mem[i-1][0] + dp_mem[i-1][1]
    dp_mem[i][1] = dp_mem[i-1][0]
    
print(sum(dp_mem[n]))
