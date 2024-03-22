import math
def solution(fees, records):
    answer = []
    #입차와 출차 기록이 존재 한다, 차량별로 주차 요금을 계산하고자 한다.
    
    rec=[]
    total_num=dict()
    total_num_list=[]
    for i in records:
        a1,a2,a3=i.split(" ")
        temp=[a1]
        a2=(int)(a2)
        temp.append(a2)
        temp.append(a3)
        rec.append(temp)
        if a2 not in total_num:
            total_num[a2]=[temp]
            total_num_list.append(a2)
        else:
            total_num[a2].append(temp)
    total_num_list.sort()
    for i in total_num_list:
        now=total_num[i]
        now=sorted(now,key=lambda x:(x[0],x[2]))
        
        price=fees[1]#기본 가격을 의미함
        time=0#얼마나 지났는지 체크할 변수임
        before=0
        for i in now:
            a1,_,a3=i
            b1,b2=a1.split(":")
            temp_time=(int)(b1)*60+(int)(b2)
            if a3=="OUT":
                time+=(temp_time)-(before)
                before=temp_time
            else:
                before=temp_time
        #print(before)
        if now[-1][2]=="IN":
            time+=(23)*60+59-(before)
        
        if time>fees[0]:
            time-=fees[0]
            #print(time)
            price+=(math.ceil(time/fees[2])*fees[3])
        
        answer.append(price)
    
        
    
    
    
    
    
    
    
    
    
    
    
    return answer