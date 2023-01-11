def measure(number):
    numbercount=[]
    for z in range(number+1):
        count=[]
        for i in range(z):
            if z%(i+1)==0:
                count.append(i)
            i+=1
        numbercount.append(len(count))
        z+=1
    numbercount.remove(0)
        
    return numbercount


def solution(number, limit, power):
    answer = 0
    count=measure(number)
    answercount=[]

    for k in range(len(count)):
        if count[k] <= limit:
            answercount.append(count[k])
        else:
            answercount.append(power)
        k+=1
                                   
    for q in range(len(answercount)):
        answer = answer + (answercount[q])
        q+=1

    return answer
