def solution(s):
    answer = []
    a = list(s)
    for i in range(len(a)):
        if i == 0 or (a[i] not in a[:i]):
            answer.append(-1)
        elif a[i] in a[:i]:
            z=-1
            while z == 0def solution(s):
    answer = []
    a = list(s)
    for i in range(len(a)):
        if i == 0 or (a[i] not in a[:i]):
            answer.append(-1)
        elif a[i] in a[:i]:
            z=-1
            while z < 0:
                if a[:i][z] == a[i]:
                    answer.append(-z)
                    z= 0
                else:
                    z-=1
            
    return answer
                if a[:i][z] == a[i]:
                    answer.append(-z)
                    z= 0
                else:
                    z-=1
            
    return answer
#프로그래머스 lv 1 가장 가까운 같은 글자
