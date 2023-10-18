def solution(targets):
    answer = 0
    t=sorted(targets,key=lambda x:(x[1],x[0]))
    now=0
    cnt=0
    for a1,a2 in t:
        if a1>=now:
            now=a2
            cnt+=1
    
    
    return cnt