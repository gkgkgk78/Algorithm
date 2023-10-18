
def solution(plans):
    answer = []
    #과제를 진행 해보자
    #과제를 끝낸 순서대로 이름을 배열에 담아 리턴을 하도록 하라
    
    #다음게 지금 끝난 시간보다 후면은 그 시간동안 작업 가능하다
    now=0
    last=[]
    plan=sorted(plans,key=lambda x: x[1])
    index=0
   
    for name,start,time in plan:
        if index==0:
            temp=list(start.split(":"))
            ti=(int)(temp[0])*60+(int)(temp[1])
            now=ti
            last.append ( (name, ti, (int)(time) ))
        else:
            temp=list(start.split(":"))
            ti=(int)(temp[0])*60+(int)(temp[1])
            #이제 시작 시간 전까지 제거 가능한것들 있으면 제거 하도록 하자
           
            while 1:
                if len(last)==0:
                    break
                name1,start1,time1=last.pop()
                time1=(int)(time1)
               
                if now+time1<=ti:
                    answer.append(name1)
                    now=now+time1
                else:
                    #남은 시간 계산하자
                    nex=ti-now
                    last.append((name1,ti,time1-nex))
                    now=ti
                    break
                if now==ti:
                    break
            now=ti
            last.append((name,ti,(int)(time)))
            
        index+=1
    while last:
        a1,a2,a3=last.pop()
   
        answer.append(a1)

    
    
    return answer