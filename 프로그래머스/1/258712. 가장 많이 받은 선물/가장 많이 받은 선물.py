def solution(friends, gifts):
    answer = 0
    #카카오톡 선물하기 기능을 이용해 축하 선물 보낼수 있다
    #다음달에 누가 선물을 많이 받을지 예측 하려고 한다
    
    index=dict()
    n=len(friends)
    for i in range(n):
        index[friends[i]]=i
    total=[[0]*(n)for _ in range(n)]
    give=[0]*(n)
    get=[0]*(n)
    for i in gifts:
        i1,i2=i.split(" ")
        a1=index[i1]
        a2=index[i2]
        total[a1][a2]+=1
        give[a1]+=1
        get[a2]+=1
    #받을거만 생각하면 됨
    for i in range(n):
        now=0
        for j in range(n):
            if j==i:
                continue
            mine=total[i][j]
            their=total[j][i]
            if mine!=0 or their!=0:
                if mine>their:
                    now+=1
                elif mine==their:
                    n1=give[i]-get[i]
                    n2=give[j]-get[j]
                    if n1>n2:
                        now+=1
                    
            else:
                n1=give[i]-get[i]
                n2=give[j]-get[j]
                if n1>n2:
                    now+=1
        answer=max(now,answer)
        
    
    return answer