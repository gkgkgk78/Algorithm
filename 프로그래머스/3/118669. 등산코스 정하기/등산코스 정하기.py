
import sys
import heapq

#dijk(gates,graph,fin,n)
def dijk(gates,graph,fin,n):
    visit=[sys.maxsize]*(n+1)
    #다익스트라 풀이
    q=[]
    for i in gates:
        visit[i]=0
        heapq.heappush(q,(0,i))
    
    while len(q)>0:
        value,vertex=heapq.heappop(q)
        if vertex in fin:
            continue
        if visit[vertex]<value:
            continue
        for ver,val in graph[vertex]:
            nex=max(val,value)
            if nex<visit[ver]:
                visit[ver]=nex
                heapq.heappush(q,(nex,ver))

    return visit
    



def solution(n, paths, gates, summits):
    answer = []
    #산봉 우리중 한곳만 방문한뒤 원래의 출입구로 돌아오는 등산코스를 정하려고 한다
    graph=[[]for _ in range(n+1)]
    la=[]
    for i in paths:
        a1,a2,a3=i
        graph[a1].append((a2,a3))
        graph[a2].append((a1,a3))
    #gates는 출입구임
    fin=dict()
    for i in summits:
        fin[i]=1
        la.append(i)
    anan=sys.maxsize
    la.sort()
    
    aa=dijk(gates,graph,fin,n)
    for i in la:
        if aa[i]<anan:
            anan=aa[i]
            answer=[i,aa[i]]
    
    
    return answer