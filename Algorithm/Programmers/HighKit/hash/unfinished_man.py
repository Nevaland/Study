def solution(participants, completion):
    temp = 0
    dic = {}
    for a_participant in participants:
        dic[hash(a_participant)] = a_participant
        temp += int(hash(a_participant))
    for com in completion:
        temp -= hash(com)
    return dic[temp]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
