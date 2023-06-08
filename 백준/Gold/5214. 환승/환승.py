import sys
from collections import deque
input = sys.stdin.readline

graph=[[]for _ in range(102000)]
visit=[0]*(102000)
now=1

n,k,m=map(int,input().split())
h1=100001
for _ in range(m):
    e=list(map(int,input().split()))

    for l in e:
        graph[l].append(h1)
        graph[h1].append(l)
    h1+=1

q=deque()
q.append((1,1))
visit[1]=1
while q:
    a1,a2=q.popleft()
    if a1==n:
        print(a2)
        sys.exit()
    
    for t1 in graph[a1]:
        if visit[t1]==0:
            for z1 in graph[t1]:
                if visit[z1]==0:
                    q.append((z1,a2+1))
                    visit[z1]=1
                if z1==n:
                    print(a2+1)
                    sys.exit()
            visit[t1]=1

print(-1)