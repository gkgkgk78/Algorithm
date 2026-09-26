import sys
from collections import deque
answer=sys.maxsize

def bfs(x1,y,n):
    global answer
    q=deque()
    visit=[-1]*(y+2)
    q.append((x1,0))
    
    while q:
        x,count=q.popleft()
        if x>y:
            continue
        if x==y:
            answer=min(answer,count)
            continue
        if count>answer:
            continue
        if x+n<=y and visit[x+n]==-1  :
            visit[x+n]=1
            q.append((x+n,count+1))
        if x*2<=y and visit[x*2]==-1  :
            visit[x*2]=1
            q.append((x*2,count+1))
        if x*3<=y and visit[x*3]==-1  :
            visit[x*3]=1
            q.append((x*3,count+1))



def solution(x, y, n):
    global answer
    bfs(x,y,n)
    if answer==sys.maxsize:
        answer=-1
    
    return answer