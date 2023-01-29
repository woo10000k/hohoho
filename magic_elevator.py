'''
def solution(storey):
    answer = 0
    storey_list = list(map(int, str(storey)))
    for i in range(len(storey_list)):
        if 10-(storey_list[i]) >= 5:
            answer += storey_list[i]
        elif 10 -(storey_list[i]) < 5:
            answer += (10-storey_list[i])
        elif 10-(storey_list[i]) == 10:
            answer += 0
    if len(storey_list)==2:
            answer += 1
            
        
    return answer
'''

def solution(storey):
    answer = 0
    storey_list = list(map(int, str(storey)))
    storey_list.reverse()

    for i in range(len(storey_list)):
        if 10-(storey_list[i]) >= 5:
            answer += (storey_list[i])
                
        elif 10 -(storey_list[i]) < 5:
            if storey_list[i+1] != 9:
                answer += (11-storey_list[i])
            elif storey_list[i+1] == 9:
                answer += (9-storey_list[i])    
        elif 10-(storey_list[i]) == 10:
            answer += 0
    return answer
   
    #9 
    
    
    #실패코드임 수정필요
    
    
    #프로그래머스 lv2 마법의 엘레베이터
