import sys

encrypted = [int(v) for v in sys.stdin.readline().strip()]
dp_mem = [0] * len(encrypted)

if encrypted[0] == 0 :
    print("0")
    exit(0)
dp_mem[0] = 1

for i in range(1, len(encrypted)):
    if encrypted[i] != 0:
        dp_mem[i] += dp_mem[i-1]

    teen = (encrypted[i-1] * 10 + encrypted[i])
    if 10 <= teen and teen <= 26:
        if i == 1: 
            dp_mem[i] += 1
        else:
            dp_mem[i] += dp_mem[i-2]
    elif teen == 0:
        print("0")
        exit(0)

print(dp_mem[-1] % 1000000)
