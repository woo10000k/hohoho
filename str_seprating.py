def solution(s):
    answer = 0
    s_list = list(s)
    s_number = 1
    n_number = 0
    i=1
    while len(s_list)>0:
        f_str = s_list[0]
        print(i)
        print("s=", s_number)
        print("n=", n_number)
        if s_number == n_number:
            s_list = s_list[i:]
            s_number = 1
            n_number = 0
            answer += 1
            i=1
        elif f_str == s_list[i]:
            s_number += 1
            i += 1
        elif f_str != s_list[i]:
            n_number += 1
            i += 1
        elif len(s_list) == 1:
            answer  += 1
            break
    
    return answer


print(solution("abracadabraaaaaa"))
