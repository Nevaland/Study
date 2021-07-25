def solution(genres, plays):
    TOTAL = 0
    FIRST = 1
    SECOND = 2
    PLAYS = 0
    ID = 1
    
    dic = {}
    bests_dic = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in dic:
            dic[genre][TOTAL] += play
            if dic[genre][FIRST][PLAYS] < play:
                old_1_plays = dic[genre][FIRST][PLAYS]
                old_1_id = dic[genre][FIRST][ID]
                dic[genre][FIRST][PLAYS] = play
                dic[genre][FIRST][ID] = i
                if dic[genre][SECOND][PLAYS] < old_1_plays:
                    dic[genre][SECOND][PLAYS] = old_1_plays
                    dic[genre][SECOND][ID] = old_1_id
            elif dic[genre][SECOND][PLAYS] < play:
                dic[genre][SECOND][PLAYS] = play
                dic[genre][SECOND][ID] = i
        else:
            dic[genre] = [play, [play, i], [0, -1]]
    dic = sorted(dic.items(), key=lambda item: item[1][TOTAL], reverse=True)
    
    answer = []
    for genre_tuple in dic:
        genre_info = genre_tuple[1]
        answer.append(genre_info[FIRST][ID])
        if genre_info[SECOND][ID] != -1:
            answer.append(genre_info[SECOND][ID])
    return answer

print(solution(	["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
