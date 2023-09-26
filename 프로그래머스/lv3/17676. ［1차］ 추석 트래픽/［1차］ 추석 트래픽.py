def solution(lines):
    answer = 0
    
    total=[]
    for i in lines:
        year ,hour,add=i.split(" ")
        tt=hour.split(":")
        time=0
        #시간
        time+=(int)(tt[0])*3600*1000
        #분
        time+=(int)(tt[1])*60000
        #초
        se,mise=tt[2].split(".")
        time+=(int)(se)*1000
        #밀리초
        time+=(int)(mise)
        nex=0
        add1=""
        if "." in add:
            add1=add.split(".")
            nex+=(int)(add1[0])*1000
            add2=add1[1][:-1]
            if len(add2)<3:
                for _ in range(3-len(add2)):
                    add2+="0"
            nex+=(int)(add2)
        else:
            add1=add[:-1]
            nex+=(int)(add1)*1000
        
        total.append([time-nex+1,time])

    for a1,a2 in total:
        temp1=0
        temp2=0
        b1=a1+1000-1
        b2=a2+1000-1
        for k1,k2 in total:
            if a1<=k1<=b1 or a1<=k2<=b1:
                temp1+=1
            elif k1<=a1<=k2 or k1<=b1<=k2:
                temp1+=1
            if a2<=k1<=b2 or a2<=k2<=b2:
                temp2+=1
            elif k1<=a2<=k2 or k1<=b2<=k2:
                temp2+=1
      
        answer=max(answer,temp1,temp2)
    
    return answer