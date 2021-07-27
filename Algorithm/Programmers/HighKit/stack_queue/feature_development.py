def solution(progresses, speeds):
    deploys = []
    deploy_day = 0
    cnt = 0
    for progress, speed in zip(progresses, speeds):
        remain_progress = (100 - progress)
        remain_day = remain_progress // speed + (1 if remain_progress % speed else 0)
        if remain_day <= deploy_day:
            cnt += 1
        else:   # Deploy without First
            deploys.append(cnt)
            cnt = 1
            deploy_day = remain_day
    return deploys[1:] + [cnt]

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
