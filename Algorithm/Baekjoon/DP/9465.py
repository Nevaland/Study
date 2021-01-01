# d[0][n] = MAX(d[1][n-1], d[1],[n-2]) + board[0][n]
# d[1][n] = MAX(d[0][n-1], d[0],[n-2]) + board[1][n]
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().split())), list(map(int, sys.stdin.readline().split()))]
    dp_mem = [[0]*(n+1) for _ in range(2)]
    dp_mem[0][1], dp_mem[1][1] = board[0][0], board[1][0]

    for i in range(2, n+1):
        dp_mem[0][i] = max(dp_mem[1][i-1], dp_mem[1][i-2]) + board[0][i-1]
        dp_mem[1][i] = max(dp_mem[0][i-1], dp_mem[0][i-2]) + board[1][i-1]

    print(max(dp_mem[0][n], dp_mem[1][n]))
