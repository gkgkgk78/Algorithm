import sys
from collections import deque

input = sys.stdin.readline

before = []
after = []
for i in range(4):
    e = list(map(str, input().rstrip()))
    before.append(e)
input().rstrip()
for i in range(4):
    e = list(map(str, input().rstrip()))
    after.append(e)

ans = ""
for i in after:
    ans += "".join(i)


def make(graph):
    t = []
    index = 0
    for i in range(4):
        temp = []
        for j in range(4):
            temp.append(graph[index])
            index += 1
        t.append(temp)
    return t

def make_str(e):
    ans=""
    for i in e:
        ans+="".join(i)
    return ans

def bfs():
    visit=dict()
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    q=deque()
    bb=make_str(before)
    q.append((bb,0))
    visit[bb]=1
    while q:
        gr,count=q.popleft()
        if gr==ans:
            print(count)
            sys.exit()
        gra=make(gr)
        for i in range(4):
            for j in range(4):
                if gra[i][j]!=after[i][j]:
                    #이제 바꿔야 함
                    now=gra[i][j]
                    for k in range(4):
                        zx=i+dx[k]
                        zy=j+dy[k]
                        be=""
                        if 0<=zx<4 and 0<=zy<4:
                            be=gra[zx][zy]
                            gra[i][j]=be
                            gra[zx][zy]=now
                            nex=make_str(gra)
                            if nex not in visit:
                                visit[nex]=1
                                q.append((nex,count+1))
                            gra[i][j] = now
                            gra[zx][zy] = be
bfs()