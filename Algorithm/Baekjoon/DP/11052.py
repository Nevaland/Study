import sys

n  = int(sys.stdin.readline())
cards = [0] + list(map(int, sys.stdin.readline().split()))
dp_mem = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp_mem[i] = max(dp_mem[i], dp_mem[i-j] + cards[j])

print(dp_mem[n])
