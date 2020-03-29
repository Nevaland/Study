import math
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(' '))
    d = math.sqrt(((x1-x2)**2 + (y1-y2)**2))

    if r1 < r2: r1, r2 = r2, r1
    print(-1 if d == 0 and r1 == r2 else
         (2 if r1-r2 < d and d < r1+r2 else 
         (1 if r1+r2 == d or r1-r2 == d else 0)))