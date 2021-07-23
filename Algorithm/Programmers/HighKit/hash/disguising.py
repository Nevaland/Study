def solution(clothes):
    dic = {}
    for a_clothes in clothes:
        clothes_type = a_clothes[1]
        if clothes_type not in dic:
            dic[clothes_type] = 2
        else:
            dic[clothes_type] += 1
    cnt = 1
    for clothes_type in dic:
        cnt *= dic[clothes_type]
    return cnt - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
