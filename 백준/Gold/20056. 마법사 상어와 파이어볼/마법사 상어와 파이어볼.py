import sys,math
input = sys.stdin.readline
class fire:
    r = -1
    c = -1
    m = 0
    d = -1
    s = -1

    def __init__(self, pa):
        self.r = pa[0]
        self.c = pa[1]
        self.m = pa[2]
        self.s = pa[3]
        self.d = pa[4]


n, m, k = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(n)]
run = []  # 현재 존재 하는 파이어 볼들이 들어갈 변수를 의미함
dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

for _ in range(m):
    e = list(map(int, input().split()))
    e[0] = e[0] - 1
    e[1] = e[1] - 1
    temp = fire(e)
    graph[e[0]][e[1]].append( temp)
    run.append((e[0], e[1]))

def make_right(x):
    if x<0:
        now=abs(x)
        return n-now
    elif x>=n:
        return x-n
    else:
        return x

for _ in range(k):
    # k번 동안 이동을 하며 파악을 하도록 해보자
    next = []
    runs=[]



    # 현재 이동 가능한 파이어 볼들을 모두 이동 시키고자 함
    visit=[[[] for _ in range(n)] for _ in range(n)]
    for sx, sy in run:
        # 현재 그래프 상에서 이동 가능한 만큼 이동 하고자 함
        ind=len(graph[sx][sy])-1
        for now in  range(len(graph[sx][sy])-1,-1,-1 ):
            # 이동후 <0일시 절댓값 변환후 n-x%n
            # 이동후 >=n일시 절댓값 x%n이면 됨
            ui=graph[sx][sy][now]
            fx, fy = dir[ui.d]
            zx = sx + fx * (ui.s%n)
            zy = sy + fy * (ui.s%n)

            if zx==-5 and zy==11:
                io=1
            # 전체 이동을 함
            zx=make_right(zx)
            zy=make_right(zy)
            put=graph[sx][sy][ind]
            if len(visit[zx][zy])>0:
                next.append((zx,zy))
            else:
                runs.append((zx,zy))
            visit[zx][zy].append(put)
            graph[sx][sy].pop(ind)
            ind-=1
    #모든 이동을 시키고 난후에
    next=set(next)
    #중복 좌표들을 없애고 난후

    for sx,sy in next:
        sumz=0
        velo=0
        di=0
        divodd=0
        diveven=0
        for l in visit[sx][sy]:
            sumz+=l.m
            velo+=l.s
            di+=l.d
            if l.d%2==0:
                divodd+=1
            elif l.d%2==1:
                diveven+=1
        mi=math.floor(sumz/5)
        ms=math.floor(velo/len(visit[sx][sy]))
        all=0
        if divodd==len(visit[sx][sy]) or diveven==len(visit[sx][sy]):
            all=1
        visit[sx][sy]=[]
        if mi >0:
            if all==1:
                for ai in [0,2,4,6]:
                    visit[sx][sy].append(fire([sx,sy,mi,ms,ai]))
            else:
                for ai in [1,3,5,7]:
                    visit[sx][sy].append(fire([sx,sy,mi,ms,ai]))
    graph=visit
    run=runs



sumz=0

for i in range(n):
    for j in range(n):
        if len(graph[i][j])>0:
            for k in graph[i][j]:
                sumz+=k.m
print(sumz)