def solution(msg):
    answer = []
    last=27
    total=dict()
    di=['A','B','C','D','E','F','G','H','I','J','K',
        'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    for i in range(len(di)):
        now=di[i]
        total[now]=i+1
    
   
    while 1:
        #사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다
        temp=msg[0]
        index=0
        for i in range(1,len(msg)):
            nex=msg[i]
            if temp+nex in total:
                temp+=nex
                index+=1
            else:
                break
        answer.append(total[temp])
        if index==len(msg)-1:
            break
        else:
            index+=1
            temp+=msg[index]
            total[temp]=last
            last+=1
            msg=msg[index:]
    
    
    return answer