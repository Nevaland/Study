def solution(brown, yellow):
    for height in range(1, yellow + 1):
        if yellow % height:
            continue
        width = int(yellow / height)
        if brown == (height * 2 + width * 2 + 4):
            return [width + 2, height + 2]
    return []
  
print(solution(24, 24))
