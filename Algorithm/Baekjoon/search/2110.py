import sys

homes = list()
n, c = map(int, sys.stdin.readline().split())
for _ in range(n):
    homes.append(int(sys.stdin.readline()))
homes.sort()

min_term = 1
max_term = homes[-1] - homes[0]

def is_enough_term(term):
    cnt = 1
    pre_home = homes[0]
    for home in homes[1:]:
        if (home - pre_home) >= term:
            cnt += 1
            pre_home = home

    return c <= cnt

while max_term - min_term > 1:
    mid_term = min_term + (max_term - min_term) // 2
    if is_enough_term(mid_term):
        min_term = mid_term
    else:
        max_term = mid_term

if is_enough_term(max_term):
    print(max_term)
else:
    print(min_term)
