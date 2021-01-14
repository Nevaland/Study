import sys

papers = list()
n = int(sys.stdin.readline())
cnts = [0, 0, 0]    # 0, 1 -1

for _ in range(n):
    papers.append(list(map(int, sys.stdin.readline().split())))

def is_clean_paper(x_pos, y_pos, size):
    value = papers[y_pos][x_pos]
    for i in range(y_pos, y_pos + size):
        for j in range(x_pos, x_pos + size):
            if papers[i][j] != value:
                return False
    return True

def divide_paper(x_pos, y_pos, size):
    size = size // 3
    divided_paper = list()
    for i in range(3):
        for j in range(3):  # 06 
            divided_paper.append((x_pos + j * size, y_pos + i * size))
    return divided_paper 
    
def solve(x_pos, y_pos, size):
    if is_clean_paper(x_pos, y_pos, size):
        cnts[papers[y_pos][x_pos]] += 1
    else:
        for x, y in divide_paper(x_pos, y_pos, size):
            solve(x, y, size // 3)

solve(0, 0, n)
print(cnts[-1])
print(cnts[0])
print(cnts[1])
