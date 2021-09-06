def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    real_reserve = (set(reserve)- set(lost))
    real_lost = (set(lost)- set(reserve))
    
    
    answer = (n-len(real_lost))
    
    for l in real_lost:

        if (l-1 in real_reserve):
            answer += 1
            real_reserve.remove(l-1)
        
        elif (l+1 in real_reserve):
            answer += 1
            real_reserve.remove(l+1)
    
    return answer
