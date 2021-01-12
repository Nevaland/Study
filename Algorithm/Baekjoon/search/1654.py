import sys

lans = list()
k, n = map(int, sys.stdin.readline().split())
for _ in range(k):
    lans.append(int(sys.stdin.readline()))

max_l = max(lans)
min_l = 1
mid_l = 0

def is_enough_cut(cut_l):
    cnt = 0
    for lan in lans:
        cnt += lan // cut_l
    return n <= cnt

while max_l - min_l > 1:    
    mid_l = min_l + (max_l-min_l) // 2
    if is_enough_cut(mid_l):
        min_l = mid_l
    else:
        max_l = mid_l

if is_enough_cut(max_l):
    print(max_l)
else:
    print(min_l)
