def solution(answers):
    markings = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    markings_len = [5, 8, 10]
    corrects = [0, 0, 0]
    for i, answer in enumerate(answers):
        for j in range(3):
            if answer == markings[j][i % markings_len[j]]:
                corrects[j] += 1

    corrector = []
    max_correct = 0
    for i, correct in enumerate(corrects):
        if max_correct < correct:
            max_correct = correct
            corrector = [i+1]
        elif max_correct == correct:
            corrector.append(i+1)
    return corrector if max_correct != 0 else [1, 2, 3]
print(solution([1,3,2,4,2]))
