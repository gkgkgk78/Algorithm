def solution(n, t, m, timetable):
    answer = ''
    bus_time=[540]
    for i in range(n-1):
        bus_time.append(bus_time[-1]+t)
    answer=0
    index=0
    time=[]
    timetable.sort()
    for i in timetable:
        a1=i.split(":")
        time.append((int)(a1[0])*60 +(int)(a1[1]))
    print(bus_time)
    for i in bus_time:
        check=0
        last=0
        #이제 체크를 해보도록 하자
        while index<len(time):
            
            if time[index]<=i:
                last=time[index]
                check+=1
                if check==m:
                    index+=1
                    break
            else:
                break
            index+=1
            if index==len(time):
                break

        
        if check<m:
            answer=i
        elif check==m:
            answer=last-1
        
    hour=answer//60
    if hour<10:
        hour="0"+str(hour)
    min=answer%60
    if min<10:
        min="0"+str(min)
    answer=(str)(hour)+":"+(str)(min)
    
    return answer