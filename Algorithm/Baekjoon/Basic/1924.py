import sys

WEK = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
MONMAX = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

x, y = map(int, sys.stdin.readline().split())
sumday = 0

for i in range(x-1):
    sumday += MONMAX[i]
sumday += y

print(WEK[(sumday % 7)])