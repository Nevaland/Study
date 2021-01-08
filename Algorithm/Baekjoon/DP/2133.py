import sys

n = int(sys.stdin.readline())
if n % 2 != 0: 
    print("0")
    exit()

n = int(n/2)
dp_mem = [0] * (n+1)
dp_mem[0] = 1
dp_mem[1] = 3

for i in range(2, n+1):
    dp_mem[i] = dp_mem[i-1] * 3
    for j in range(2, i+1):
        dp_mem[i] += 2 * dp_mem[i-j]

print(dp_mem[n])
