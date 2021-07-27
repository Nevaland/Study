def solution(bridge_length, weight_limit, truck_weights):
    sec_cnt = 0
    trucks_weight_in_bridge = [0] * bridge_length
    trucks_num_in_bridge = 0
    now_weight = 0
    truck_weight = 0
    while truck_weights or truck_weight:
        if not truck_weight:
            truck_weight = truck_weights.pop(0)
            
        if trucks_weight_in_bridge[sec_cnt % bridge_length]:
            now_weight -= trucks_weight_in_bridge[sec_cnt % bridge_length]
            trucks_weight_in_bridge[sec_cnt % bridge_length] = 0
            trucks_num_in_bridge -= 1
            
        if (now_weight + truck_weight) <= weight_limit and (trucks_num_in_bridge + 1) <= bridge_length:
            trucks_weight_in_bridge[sec_cnt % bridge_length] = truck_weight
            trucks_num_in_bridge += 1
            now_weight += truck_weight
            truck_weight = 0
            
        sec_cnt += 1
    return sec_cnt + bridge_length

print(solution(2, 10, [7, 4, 5, 6]))
