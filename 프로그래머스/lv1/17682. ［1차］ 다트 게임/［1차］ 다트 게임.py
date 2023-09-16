def solution(dartResult):
    answer = 0
    #다트를 세차례 던져 점수의 합계로 실력을 겨룬다
    
    #각 기회마다 얻을수 있는 점수는 0점에서 10점 사이다
    test=dartResult
    #점수 보너스 옵션 으로 문자열이 이루어져 있다
    ans=[]
    number=["0","1","2","3","4","5","6","7","8","9"]
    i=0
    
    while i<len(test):
        now=""
        if test[i]=="1":
            if test[i+1]=="0":
                i+=1
                now="10"
            else:
                now=test[i]
        else:
            now=test[i]

        now=(int)(now)
        i+=1
        if test[i]=="D":
            now=now**2

        elif test[i]=="T":
            now=now**3
        
        if i+1<len(test):
            if test[i+1]=="*" or test[i+1]=="#":
                if test[i+1]=="*":
                    if len(ans)>0:
                        ans[-1]=ans[-1]*2
                    now=now*2

                elif test[i+1]=="#":
                    now=-now 
                i+=1
        i+=1
        ans.append(now)
        
                    
    answer=sum(ans)

    
    
    return answer