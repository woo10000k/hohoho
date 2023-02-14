def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = n-len(lost)
    imsi=[]
    i=0
    while i<len(lost):
        if reserve.count(lost[i]) == 1:
            reserve.remove(lost[i])
            imsi.append(lost[i])
            answer += 1
            i += 1
        else:
            i += 1  
    
    lost = [x for x in lost if x not in imsi]
    
    i=0
    while i<len(lost):
        if reserve.count(lost[i]-1) == 1:
            reserve.remove(lost[i]-1)
            answer += 1
            i += 1
        elif reserve.count(lost[i]+1) == 1:
            reserve.remove(lost[i]+1)
            answer += 1
            i += 1
    
        else:
            i += 1
    
    return answer


#프로그래머스 lv1 체육복 (탐욕법Greedy)
#!!
