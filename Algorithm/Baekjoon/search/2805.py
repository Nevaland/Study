import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

min_h = 0
max_h = max(trees)
h = 0

def is_enough_cut(cut_h):
    cnt = 0
    for tree in trees:
        cnt += tree - cut_h if tree > cut_h else 0
    return cnt >= m

while max_h - min_h > 1:
    mid_h = min_h + (max_h - min_h) // 2
    if is_enough_cut(mid_h):
        min_h = mid_h
    else:
        max_h = mid_h

print(min_h)
