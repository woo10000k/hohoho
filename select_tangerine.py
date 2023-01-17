def solution(k, tangerine):
    answer = 0
    tangerine_dict = {}
    for i in range(len(tangerine)):
        if tangerine[i] not in tangerine_dict:
            tangerine_dict[tangerine[i]] = 1
        elif tangerine[i] in tangerine_dict:
            tangerine_dict[tangerine[i]] +=1



    while k>=1:
        tan_max=tangerine_dict[max(tangerine_dict, key=tangerine_dict.get)]
#        print(tan_max)
        k = k-(tan_max)
        print(k)
        tangerine_dict.pop(max(tangerine_dict, key=tangerine_dict.get))
        answer +=1
        
    return answer
                           
                           
#프로그래머스 lv2 귤고르기
#시간
