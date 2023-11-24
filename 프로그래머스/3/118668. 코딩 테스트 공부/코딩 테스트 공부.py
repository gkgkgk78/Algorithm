import heapq
import sys

def dijk(x,y,alp,cop,total,visit):
    answer=sys.maxsize
    q=[]
    visit[x][y]=0
    heapq.heappush(q,(0,x,y))
    while q:
        time,x,y=heapq.heappop(q)
        
        if x>=alp and y>=cop:
            answer=min(answer,time)
            continue
        if visit[x][y]<time:
            continue
        #print(time,x,y)
        for a1,a2,a3,a4,a5 in total:
            if x>=a1 and y>=a2:
                #print("하이")
                nex=time+a5
                xx=x+a3
                yy=y+a4
                if xx>=150:
                    xx=150
                if yy>=150:
                    yy=150
                if visit[xx][yy]>nex:
                    visit[xx][yy]=nex
                    heapq.heappush(q,(nex,xx,yy))
        
    return answer        
    

def solution(alp, cop, problems):
    answer = 0
    #그럼 생각을 해보도록 하자
    total=[]
    x=-1
    y=-1
    visit=[[sys.maxsize]*(151)for _ in range(151)]
    for a1,a2,a3,a4,a5 in problems:
        if a3==0 and a4==0:
            continue
        total.append((a1,a2,a3,a4,a5))
        x=max(x,a1)
        y=max(y,a2)
    total.append((0,0,1,0,1))
    total.append((0,0,0,1,1))
    
    #(x,y,alp,cop,total,visit):
    answer=dijk(alp,cop,x,y,total,visit)
    
    
    return answer