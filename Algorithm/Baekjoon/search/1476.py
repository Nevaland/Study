import sys

E, S, M = map(int, sys.stdin.readline().split())

cnt = 1
e, s, m = 1, 1, 1

while (e, s, m) != (E, S, M):
    cnt += 1
    
    e += 1
    if 15 < e:
        e = 1

    s += 1
    if 28 < s:
        s = 1

    m += 1
    if 19 < m:
        m = 1

print(cnt)
