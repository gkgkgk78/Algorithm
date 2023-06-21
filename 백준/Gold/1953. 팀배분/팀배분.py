import sys
from collections import deque
input = sys.stdin.readline


n=int(input().rstrip())
graph=[[]for _ in range(n+1)]
visit=[0]*(n+1)
color=[-1]*(n+1)
for l in range(1,n+1):
    e=list(map(int,input().split()))
    for i in range(1,len(e)):
        graph[l].append(e[i])

def bfs(l):
    global color
    q = deque()
    visit[l]=1
    q.append((l,0))
    color[l]=0

    while q:
        vertex,co=q.popleft()
        for t1 in graph[vertex]:
            if visit[t1]==0:
                next=-1
                if co==0:
                    next=1
                else:
                    next=0
                color[t1]=next
                visit[t1]=1
                q.append((t1,next))


for l in range(1,n+1):
    if visit[l]==0:
        bfs(l)


blue=[]
red=[]
for l in range(1,n+1):
    if color[l]==0:
        blue.append(l)
    else:
        red.append(l)

blue.sort()
red.sort()
print(len(blue))
print(*blue)
print(len(red))
print(*red)