import sys

n = int(sys.stdin.readline())
dp_mem = [0] * (n+1)

for i in range(1,n+1):
    j = 1
    while j*j <= i:
        if dp_mem[i] > dp_mem[i - j*j] + 1 or dp_mem[i] == 0:
            dp_mem[i] = dp_mem[i - j*j] + 1
        j += 1

print(dp_mem[n])
