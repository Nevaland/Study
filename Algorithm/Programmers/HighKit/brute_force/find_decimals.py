from itertools import permutations

def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        answer |= set(map(int, map("".join, permutations(list(numbers), i + 1))))
    answer -= set(range(0, 2))
    
    for i in range(2, int(max(answer) ** 0.5) + 1):
        answer -= set(range(i * 2, max(answer) + 1, i))
            
    return len(answer)

print(solution("011"))
