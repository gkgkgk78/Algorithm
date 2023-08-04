from collections import deque

def solution(x, y, n):
    answer = -1
    q=deque()
    visit=[0]*(y+1)
    visit[x]=1
    q.append((x,0))
    while q:
        a1,time=q.popleft()
        if a1==y:
            answer=time
            break
        temp=[]
        temp.append(a1+n)
        temp.append(a1*2)
        temp.append(a1*3)
        for i1 in temp:
            if i1>y:
                continue                
            if visit[i1]==0:
                visit[i1]=1
                q.append((i1,time+1))
    

    return answer