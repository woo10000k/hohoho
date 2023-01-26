def solution(t, p):
    answer = 0
    t_list = list(t)
    p_list = list(p)
    for i in range(len(t_list)-len(p_list)+1):
        t_str = ""
        for i in range(i, i+len(p_list)):
            t_str += t_list[i]

        t_int = int(t_str)
        p_int = int(p)
        if t_int <= p_int:
            answer += 1
        
    return answer

#프로그래머스 lv1 크기가 작은 부분 문자
