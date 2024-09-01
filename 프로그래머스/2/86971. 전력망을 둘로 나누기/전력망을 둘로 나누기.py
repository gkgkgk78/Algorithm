from collections import deque
import sys

def bfs(start,ind,visit,graph,v1,v2):
    visit[start]=ind
    q=deque()
    q.append(start)
    while q:
        a1=q.popleft()
        for i in graph[a1]:
            if v1==a1 and v2==i:
                continue
            if v1==i and v2==a1:
                continue
            if visit[i]==0:
                visit[i]=ind
                q.append(i)
                


def solution(n, wires):
    answer = sys.maxsize
    #전력망을 2개로 분할 하려고 한다
    # 두 전력 망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 한다
    #송전탑 개수, 전선 정보 가 매개 변수로 주어진다
    graph=[[]for _ in range(n+1)]
    for a1,a2 in wires:
        graph[a1].append(a2)
        graph[a2].append(a1)
    
    for a1,a2 in wires:
        #이제 이 두 정점을 있는 거를 위주로 작업해 보도록 하자
        visit=[0]*(n+1)
        visit[0]=-1
        ind=1
        check=0
        for i in range(1,len(visit)):
            if visit[i]==0:
                bfs(i,ind,visit,graph,a1,a2)
                ind+=1
            if ind >=4:
                check=1
                break
        if check==0:
            a1=visit.count(1)
            a2=visit.count(2)
            answer=min(answer,abs(a1-a2))
                
    
    return answer
    
    