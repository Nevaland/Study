# D[i] = D[i-5] + D[i-1]
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    dp_mem = [1] + [0] * n

    for i in range(1, n+1):
        if i < 6:
            if i == 4:
                dp_mem[i] = dp_mem[i-3] + dp_mem[i-1]
            else:
                dp_mem[i] = dp_mem[i-1]
        else:
            dp_mem[i] = dp_mem[i-5] + dp_mem[i-1]

    print(dp_mem[n])
exit(0)
