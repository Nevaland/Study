import sys

n, m = map(int, sys.stdin.readline().split())
a_arr = list(map(int, sys.stdin.readline().split()))
b_arr = list(map(int, sys.stdin.readline().split()))

# print(' '.join(map(str, sorted(a_arr + b_arr))))

a_i = 0
b_i = 0
total_arr = list()
for _ in range(n + m):
    if a_arr[a_i] < b_arr[b_i]:
        total_arr.append(a_arr[a_i])
        a_i += 1
        if a_i == n:
            total_arr += b_arr[b_i:]
            break
    else:
        total_arr.append(b_arr[b_i])
        b_i += 1
        if b_i == m:
            total_arr += a_arr[a_i:]
            break
        
print(' '.join(map(str, total_arr)))
