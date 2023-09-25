from collections import deque
def change(val,n):
    
    ee=deque()
    vv=val
    if val==0:
        ee.append(0)
        return ee
    while vv:
        second=vv%n
        ee.appendleft(second)
        vv=vv//n

    return ee



def solution(n, t, m, p):
    answer = ''
    
    total=dict()
    total[10]="A"
    total[11]="B"
    total[12]="C"
    total[13]="D"
    total[14]="E"
    total[15]="F"
    
    now=0
    cou=1
    chch=0
    while 1:
        #우선 진법 변환
        aa=change(now,n)
        
        while aa:
            a1=aa.popleft()
            nex=""
            if a1<10:
                nex=(str)(a1)
            else:
                nex=total[a1]
            if cou==p:
                answer+=nex
                chch+=1
            if chch==t:
                return answer
            cou+=1
            if cou==m+1:
                cou=1
        now+=1
    
    
    
    
    return answer