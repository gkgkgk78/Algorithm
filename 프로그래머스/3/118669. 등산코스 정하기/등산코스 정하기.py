from collections import deque
import sys
def start_to(gates,graph,start,fin,n,val):
    visit=[0]*(n+1)
    #이렇게 해서 가능한지를 파악 해야 한다
    #최소한 가능하려면 val 보다 커야 가능할테니
    #가고 오고 모두 가능해야 한다
    #가장긴 시간보다 작은거로 이동 가능하면 되는데.....
    #가장 길었던 거를 표기 해주면 될듯 하다, 그러면 처리 되지 않을까?
    q=deque()
    for i in gates:
        visit[i]=1
        q.append((i,0))#지금까지 가장 길었던거를 명시해 줄거임
    while q:
        a1,va=q.popleft()
        if a1 in fin:
            continue
        for a1,a2 in graph[a1]:
            if visit[a1]==0 and a2<=val:
                visit[a1]=1
                q.append((a1,visit[a1]))
    return visit
    



def solution(n, paths, gates, summits):
    answer = []
    #산봉 우리중 한곳만 방문한뒤 원래의 출입구로 돌아오는 등산코스를 정하려고 한다
    graph=[[]for _ in range(n+1)]
    right=0
    for i in paths:
        a1,a2,a3=i
        graph[a1].append((a2,a3))
        graph[a2].append((a1,a3))
        right=max(right,a3)
    #gates는 출입구임
    #summits는 산봉우리임
    start=dict()
    fin=dict()
    la=[]
    for i in gates:
        start[i]=1
    for i in summits:
        fin[i]=1
        la.append(i)
    left=0
    right+=1
    anan=sys.maxsize
    la.sort()
    while left+1<right:
        #모든 게이트에서 출발한다?
        mid=(left+right)//2
        aa=start_to(gates,graph,start,fin,n,mid)
        #이제 체크를 해보도록 하자
        tt=-1
        for i in la:
            if aa[i]!=0:
                tt=i
                break
                
        if tt!=-1:
            right=mid
            if mid<anan:
                anan=mid
                answer=[tt,mid]
        else:
            left=mid
    
    
    return answer