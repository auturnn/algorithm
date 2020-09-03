
def solution(progresses, speeds):
    answer = []
    days = []
    
    for i in range(len(progresses)):
        days.append(-(progresses[i]-100) / speeds[i])
        
    lst = days[0]
    cnt = 1
    
    for i in days[1:]:
        if lst < i:
            answer.append(cnt)
            lst = i
            cnt = 1
            
        else :
            cnt += 1
            
    answer.append(cnt)

    return answer

print(solution([95, 95, 95, 95],[4, 3, 2, 1]),end='\n\n')
# print(solution([0,0,0,0],[0,0,0,0])) -> 문제에서 자연수라고 하였기에 제외.
print(solution([99,99,95,99],[1,1,1,100]),end='\n\n')
print(solution([0,0,0,0],[1,1,1,1]),end='\n\n')