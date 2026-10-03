
def solution(plans):
    answer = []
    for i in range (len(plans)):
        i1,i2,i3=plans[i]
        hour,mi=i2.split(":")
        plans[i]=[i1,(int)(hour)*60+(int)(mi),(int)(i3)]
    plans=sorted(plans, key=lambda x:(x[1]))
    nowTime=plans[0][1]
    
    plays=[plans[0]]
    plans=plans[1:]
 
    
    for name,start,playTime in plans:
        temp=start
        if len(plays)>0:
            while 1:
                #이제 제거 해야지
                if (len(plays)==0):
                    break
                bname,bstart,bplayTime=plays.pop()
                nex=nowTime+bplayTime
                if nex<=start:
                    nowTime=nex
                    answer.append(bname)
                    if nex==start:
                        break
                else:
                    plays.append([bname,bstart,bplayTime-(start-nowTime)])
                    break
        plays.append([name,start,playTime])
        nowTime=start
    
    while plays:
        bname,bstart,bplayTime=plays.pop()
        answer.append(bname)
    
    
    
    return answer