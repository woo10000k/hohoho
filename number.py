def solution(X, Y):
    answer = ''
    x = [int(a) for a in str(X)]
    y = [int(b) for b in str(Y)]
    XYlist=[]
    newXYlist=[]
    for i in range(len(x)):
        for k in range(len(y)):
            if x[i]==y[k]:
                XYlist.append(y[k])
            
    set(XYlist)
    oldXYlist=list(XYlist)
    

    if not newXYlist:
        newXYlist=[-1]
    
    newXYlist.sort(reverse=True)
    answerlist=(map(str,newXYlist))
    for s in answerlist:
        answer += s + ''
    return answer
