def solution(msg):
    answer = []
    
    total=dict()
    alpha=["","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(1,27):
        total[alpha[i]]=i
    index=0
    go=27
    while 1:
        #우선 들어 있는 것까지 최대로 확인 해보자구
        ee=""
        check=0
        cc=index
        inin=""
        ouou=""
        for i in range(cc,len(msg)):
            ee+=msg[i]
            if ee not in total:
                check=1
                ouou+=msg[i]
                break
            index+=1
            inin+=msg[i]
        #print(ee,check)
        #들어 있었다면
        if check==0:
            answer.append(total[inin+ouou])
        #들어 있지 않았다면
        else:
            answer.append(total[inin])
            total[inin+ouou]=go
            go+=1
        #이제 다음 으로 넘어 가야 한다
        if index>=len(msg):
            break
        
        
        
    
    
    return answer