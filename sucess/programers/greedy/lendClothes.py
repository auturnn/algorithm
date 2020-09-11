
n = 8
l = [3, 4, 7, 8]
r = [1, 2, 3, 4, 5, 7, 8]

def solution(n, lost, reserve):
    r = reserve.copy()
    n = n - len(lost)
    
    for i in r:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
            n += 1

    for i in reserve:
        if i-1 in lost :
            lost.remove(i-1)
            n += 1
        elif i+1 in lost:
            lost.remove(i+1)
            n += 1
    return n

print(solution(n,l,r))