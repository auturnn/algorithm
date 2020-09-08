def solution(bridge_length, weight, truck_weights):
    on_truck = [0] * bridge_length
    time = 0

    while True:
        if on_truck:
            on_truck.pop(0)
        else :
            break

        time += 1

        if truck_weights:
            if sum(on_truck) + truck_weights[0] <= weight:
                on_truck.append(truck_weights.pop(0))
            else:
                on_truck.append(0)

    return time


print(solution(2,10,[7,4,5,6]))