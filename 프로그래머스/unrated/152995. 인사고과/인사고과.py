def solution(scores):
    answer = 0
    s1,s2=scores[0][0],scores[0][1]
    scores=sorted(scores,key=lambda x:(-x[0],x[1]) )
    ma=scores[0][1]
    for i in range(1,len(scores)):

        if scores[i][1]<ma:
            if scores[i][0]==s1 and scores[i][1]==s2:
                return -1
            else:
                scores[i][0]=-1
                scores[i][1]=-1
        else:
            ma=scores[i][1]
                
    scores=sorted(scores,key=lambda x:-(x[0]+x[1]))
    

    before=-1
    count=1
    idx=0
    for a1,a2 in scores:
        idx+=1
        if before==-1:
            before=a1+a2
        if before!=a1+a2:
            count=idx
            before=a1+a2
        if a1==s1 and a2==s2:
            return count
    
    return answer