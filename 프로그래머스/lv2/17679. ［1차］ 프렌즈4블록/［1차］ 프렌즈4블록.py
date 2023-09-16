from collections import deque

def bfs(x,y,board,n,m):
    
    visit=[[0]*(m)for _ in range(n)]
    dx=[0,1,1]
    dy=[1,0,1]
    now=board[x][y]
    visit[x][y]=1
    q=deque()
    #이제 계속 해서 탐색을 해보도록 하지'
    #우선 첫번째 조건
    t=0
    for i in range(3):
        zx=x+dx[i]
        zy=y+dy[i]
        if 0<=zx<n and 0<=zy<m:
            if board[zx][zy]==now:
                q.append((zx,zy))
                visit[zx][zy]=1
            else:
                t=1
                break
        else:
            t=1
            break
            
    if t==1:
        return 0
    else:
        #이제 계속 탐색을 해보도록 하자
        while q:
            a1,a2=q.popleft()
            temp=deque()
            for i in range(3):
                zx=a1+dx[i]
                zy=a2+dy[i]
                if 0<=zx<n and 0<=zy<m:
                    if board[zx][zy]==now:
                        temp.append((zx,zy))
            if len(temp)==3:
                for a1,a2 in temp:
                    if visit[a1][a2]==0:
                        visit[a1][a2]=1
                        q.append((a1,a2))
    count=0
    for i in range(n):
        for j in range(m):
            if visit[i][j]==1:
                count+=1
                board[i][j]="-1"
    
    return count
    

def check(n,m,board):
    
    count=0
    for i in range(n):
        for j in range(m):
            if board[i][j]=="-1":
                continue
            v=bfs(i,j,board,n,m)

            count+=v
            
    
    return count


def down(board,n,m):
    
    for j in range(m):
        for i in range(n-2,-1,-1):
            #이제 내리기 시작할 거다
            if board[i][j]!="-1" and board[i+1][j]=="-1":
                #이제 계속 내려가야지
                x=i+1
                y=j
                while 1:
                    if x==n-1:
                        break
                    if board[x+1][j]=="-1":
                        x+=1
                    else:
                        break
                board[x][y]=board[i][j]
                board[i][j]="-1"
                
    
    


def solution(n, m, board):
    answer = 0
    
    te=[]
    for i in (board):
        e=list(map(str,i.rstrip()))
        te.append(e)
    board=te
    time=0
    while 1:
        count=check(n,m,board)
        answer+=count
        if count==0:
            break
        
        down(board,n,m)

    
    
    return answer