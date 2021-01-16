import sys

n, k = map(int, sys.stdin.readline().split())
cnt = 0

coins = list()
for i in range(n):
    coins.append(int(sys.stdin.readline()))
coins.reverse()

while k != 0:
    for coin in coins:
        if coin <= k:
            quotient = k // coin
            cnt += quotient
            k -= quotient * coin

print(cnt)
