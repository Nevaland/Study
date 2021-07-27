def solution(priorities, location):
    tasks = [[] for _ in range(10)]
    for i, priority in enumerate(priorities):
        tasks[priority].append(i)
        
    cnt = 0
    now_location = 0
    for task_indexs in reversed(tasks):
        pre_location = now_location
        if len(task_indexs) == 0:
            continue
        elif len(task_indexs) == 1:
            now_location = task_indexs[0]
            cnt += 1
            if now_location == location:
                return cnt
        else:
            next_location = task_indexs[-1]
            start_index = 0
            for i, task_index in enumerate(task_indexs):
                if now_location <= task_index:
                    start_index = i
                    break
                else:
                    next_location = task_index
                    
            checked = 0
            i = start_index
            while checked < len(task_indexs):
                if task_indexs[i % len(task_indexs)] == location:
                    return cnt + checked + 1
                else:
                    checked += 1
                    i += 1
            cnt += checked
            now_location = next_location
    return cnt

print(solution([2, 1, 3, 2], 2))
