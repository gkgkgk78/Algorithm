from itertools import permutations
import copy

def cal(a1,a2,op):
    if op=="+":
        return a1+a2
    elif op=="-":
        return a1-a2
    else:
        return a1*a2



def solution(expression):
    answer = 0
    #라이언은 우승자에게 상금 지급하는 중이다
    #연산자 우선 순위를 정할수 있다
    la=["+","-","*"]
    number=[]
    operator=[]
    temp=""
    for i in expression:
        if i in la:
            if len(temp)>0:
                number.append((int)(temp))
            temp=""
            operator.append(i)
        else:
            temp+=i
    if len(temp)>0:
        number.append((int)(temp))    
    #print(number,operator)
    ne=list(set(la))
    next=list(permutations(ne,len(ne)))
    #이제 우선 순위 대로 해서 진행 해보자
    for i in next:
        a1=i[0]
        a2=i[1]
        a3=i[2]
        
        number1=copy.deepcopy(number)
        operator1=copy.deepcopy(operator)
        #이제 우선 순위에 따라서 진행을 해보도록 하자
        ch=0
        #print(a1,a2,a3)
        #print(number1)
        while 1:
            ch=0
            for i in range(len(operator1)):
                if operator1[i]==a1:
                    z1=number1[i]
                    z2=number1[i+1]
                    z3=cal(z1,z2,operator1[i])
                    number1[i]=z3
                    del number1[i+1]
                    del operator1[i]

                    ch=1
                    break
            if ch==0:
                break
        #print(number1)
        while 1:
            ch=0
            for i in range(len(operator1)):
                if operator1[i]==a2:
                    z1=number1[i]
                    z2=number1[i+1]
                    z3=cal(z1,z2,operator1[i])
                    number1[i]=z3
                    del number1[i+1]
                    del operator1[i]
                    ch=1
                    break
            if ch==0:
                break
        #print(number1)
        while 1:
            ch=0
            for i in range(len(operator1)):
                if operator1[i]==a3:
                    z1=number1[i]
                    z2=number1[i+1]
                    z3=cal(z1,z2,operator1[i])
                    number1[i]=z3
                    del number1[i+1]
                    del operator1[i]
                    ch=1
                    break
            if ch==0:
                break
        #print(number1)
        answer=max(answer,abs(number1[0]))
    
    
    return answer