
import sys
sys.setrecursionlimit(10**6)
from collections import deque
answer=sys.maxsize
def dfs(x,y,first,rotate,board,n,m):
    global answer 
    visit=[ [[sys.maxsize]*(4)for _ in range(m)] for _ in range(n)]
    q=deque()
    for i in range(4):
        visit[0][0][i]=1
        q.append((0,0,i,0,0))
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    while q:
        x,y,dir,first,rotate=q.popleft()
        if x==n-1 and y==m-1:
            answer=min(answer,first*100+rotate*500)
            continue
        for i in range(4):
            zx=dx[i]+x
            zy=dy[i]+y
            if 0<=zx<n and 0<=zy<m and board[zx][zy]==0:
                #이제 갈수 있는 것이니 가보도록 하자
                if i==dir:
                    temp=(first+1)*100+rotate*500
                    if temp<visit[zx][zy][i]:
                        visit[zx][zy][i]=temp
                        q.append((zx,zy,i,first+1,rotate))
                else:
                    temp=(first+1)*100+(rotate+1)*500
                    if temp<visit[zx][zy][i]:
                        visit[zx][zy][i]=temp
                        q.append((zx,zy,i,first+1,rotate+1))



def solution(board):
    global answer
    n=len(board)
    m=len(board[0])
    dfs(0,0,0,0,board,n,m)
    
    
    
    
    return answer