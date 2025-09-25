def solution(participant, completion):
    answer = ''
    total=dict()
    for i in completion:
        if i not in total:
            total[i]=1
        else:
            total[i]+=1
    
    for i in participant:
        if i not in total:
            return i
        else:
            total[i]-=1
            if total[i]<0:
                return i