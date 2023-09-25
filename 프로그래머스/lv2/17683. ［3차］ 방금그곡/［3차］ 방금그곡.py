import heapq


def solution(m, musicinfos):
    answer = ''
    q=[]
   
    c=0
    m=m
    m=m.replace("C#","c")
    m=m.replace("D#","d")
    m=m.replace("F#","f")
    m=m.replace("G#","g")
    m=m.replace("A#","a")
            
    for i in musicinfos:
        s1,s2,title,mou=i.split(",")
        first=s1.split(":")
        mm=0
        mou=mou.replace("C#","c")
        mou=mou.replace("D#","d")
        mou=mou.replace("F#","f")
        mou=mou.replace("G#","g")
        mou=mou.replace("A#","a")
        first_hour,first_min=(int)(s1.split(":")[0]),(int)(s1.split(":")[1])
        second_hour,second_min=(int)(s2.split(":")[0]),(int)(s2.split(":")[1])
        now=second_hour*60+second_min-first_hour*60-first_min
        nex=""
        fi=now//len(mou)
        fl=now%len(mou)
        last=[]

        for i in range(fi):
            nex+="".join(mou)
            
        nex+="".join(mou)[:fl]
        
       
        if m in nex:
            heapq.heappush(q,(-now,c,title))
        c+=1
        
    if len(q)>0:    
        aa=heapq.heappop(q)
        answer=aa[2]
    else:
        answer="(None)"
    
    
    
    return answer