def solution(routes):
    answer = 0
    
    #그리디
    r=sorted(routes,key=lambda x:(x[1],x[0]))
    cnt=0
    ans=0
    now=-300001
    for a1,a2 in r:
        if a1>now:
            cnt+=1
            now=a2
    
    return cnt    
    
    
    return answer