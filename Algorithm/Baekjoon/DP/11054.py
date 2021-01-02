import sys

n = int(sys.stdin.readline())
table = list(map(int, sys.stdin.readline().split()))
dp_mem = [[1,1] for _ in range(n)]

for i in range(n):
    for j in range(i):
        if table[j] < table[i]:
            dp_mem[i][0] = max(dp_mem[i][0], dp_mem[j][0] + 1)
        elif table[j] > table[i]:
            dp_mem[i][1] = max(dp_mem[i][1], dp_mem[j][0] + 1)
            dp_mem[i][1] = max(dp_mem[i][1], dp_mem[j][1] + 1)
            
print(max(max(x1, x2) for x1, x2 in dp_mem))
