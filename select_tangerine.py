def solution(k, tangerine):
    answer = 0
    tangerine_dict = {}
    for i in range(len(tangerine)):
        if tangerine[i] not in tangerine_dict:
            tangerine_dict[tangerine[i]] = 1
        elif tangerine[i] in tangerine_dict:
            tangerine_dict[tangerine[i]] +=1

    tangerine_dict_list=list(tangerine_dict.values())
    tangerine_dict_list.sort(reverse=True)
    i=0
    while k>=1:
        k -=tangerine_dict_list[i]
        answer +=1
        i +=1
            

'''
    while k>=1:
        tan_max=tangerine_dict[max(tangerine_dict, key=tangerine_dict.get)]
#        print(tan_max)
        k = k-(tan_max)
        print(k)
        tangerine_dict.pop(max(tangerine_dict, key=tangerine_dict.get))
        answer +=1
        
    return answer
'''           
                           
#프로그래머스 lv2 귤고르기
#시간초과

#while 돌기 전에 dict 에서 value -> list -> sort 후 while // 시간 통과
#아래 내용은 value 최대값을 계속 찾아야 하기 때문에 dict를 while 돌때마다 탐색, 미리 정렬해 놓으면 한번만 탐색후 1 
#...
