def solution(N, stages):
    answer = []
    
    #스테이지의 개수 n은
    total=dict()
    #도달한 사람을 어떻게 구하면 좋을까?
    now=[0]*(N+3)
    for i in stages:
        now[1]+=1
        now[i+1]-=1
        if i not in total:
            total[i]=0
        total[i]+=1
        
    for i in range(2,N+1):
        now[i]+=now[i-1]
    ans=[]
    for i in range(1,N+1):
        ne=0
        if now[i]==0 or i not in total:
            ans.append((i,0))
        else:
            ans.append((i,total[i]/now[i]))
            
    ans=sorted(ans,key=lambda x:(-x[1],x[0]))

    for a1,a2 in ans:
        answer.append(a1)
    
    
    
    
    
    
    return answer