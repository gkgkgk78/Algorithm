import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
e = list(map(int, input().split()))

time = 0


def make_sqare(up):
    # row가 적은지 col이 적은지 확인을 하도록 하자
    row = len(up[0])
    col = len(up)
    next = abs(row - col)
    if row != col:
        if row < col:
            for i in up:
                for j in range(next):
                    i.append(-1)
        else:
            for j in range(next):
                tt=[-1]*(row)
                up.append(tt)
    return up

def rotate(up):
    k=len(up)
    temp=[[-1]*(k) for _ in range(k)]

    for i in range(k):
        for j in range(k):
            temp[i][j]=up[k-j-1][i]

    for i in range(len(up)-1,-1,-1):
        if -1 in temp[i]:
            temp.pop(i)
        else:
            break
    return temp
def rotate1(up):
    k=len(up)
    temp=[[-1]*(k) for _ in range(k)]

    for i in range(k):
        for j in range(k):
            temp[i][j]=up[k-j-1][i]
    t=[]
    for i in temp:
        e1=[]
        for l in range(len(i)):
            if i[l]!=-1:
                e1.append(i[l])
        if len(e1)>0:
            t.append(e1)
    return t
def make_sqare1(up,e):
    # row가 적은지 col이 적은지 확인을 하도록 하자
    n=len(e)
    temp=[]

    for i in range(len(up)-1):
        now=up[i]
        for j in range(n):
            now.append(-1)
        temp.append(now)
    last=up[-1]
    while e:
        last.append(e.popleft())
    temp.append(last)


    return temp


def up_move(e1):
    # 이제 궁중 부양을 진행 할거임

    up = []
    e = deque(e1)
    up.append([e.popleft()])  # 가장 왼쪽에꺼 뺀거임

    while 1:
        # 이제 2개이상이 될것들을 추리는 단계가 될거임
        temp = []
        for l in range(len(up[0])):
            temp.append(e.popleft())
        # 이제 뺐으니
        up.append(temp)
        #회전 시킬수 있는지 없는지 판단
        if len(up)<=len(e):
            up = make_sqare(up)
            up = rotate(up)
        else:
            break
    up=make_sqare1(up,e)
    return up


def first_eat(e):
    a = min(e)
    for i in range(n):
        if e[i] == a:
            e[i] += 1
    return e



def delete_fish(up):
    n=len(up)
    visit=[[0]*(n)for _ in range(n)]
    #이제 모든 물고기는 동시에 움직이게 될거임
    graph=[[0]*(n)for _ in range(n)]
    dx=[0,-1,0,1]
    dy=[-1,0,1,0]
    for i in range(n):
        for j in range(n):
            if up[i][j]!=-1 and visit[i][j]==0:
                visit[i][j]=1
                for l in range(4):
                    zx=i+dx[l]
                    zy=j+dy[l]
                    if 0<=zx<n and 0<=zy<n:
                        if visit[zx][zy]==0 and up[zx][zy]!=-1:
                            n1=up[i][j]
                            n2=up[zx][zy]
                            next=(abs)(n1-n2)//5
                            if next>0:
                                if n1>n2:
                                   graph[zx][zy]+=next
                                   graph[i][j]-=next
                                else:
                                    graph[zx][zy] -= next
                                    graph[i][j] += next
    for i in range(n):
        for j in range(n):
            up[i][j]+=graph[i][j]
    return up

def delete_fish(up):
    n=len(up)
    c=len(up[0])
    visit=[[0]*(c)for _ in range(n)]
    #이제 모든 물고기는 동시에 움직이게 될거임
    graph=[[0]*(c)for _ in range(n)]
    dx=[0,-1,0,1]
    dy=[-1,0,1,0]
    for i in range(n):
        for j in range(c):
            if up[i][j]!=-1 and visit[i][j]==0:
                visit[i][j]=1
                for l in range(4):
                    zx=i+dx[l]
                    zy=j+dy[l]
                    if 0<=zx<n and 0<=zy<c:
                        if visit[zx][zy]==0 and up[zx][zy]!=-1:
                            n1=up[i][j]
                            n2=up[zx][zy]
                            next=(abs)(n1-n2)//5
                            if next>0:
                                if n1>n2:
                                   graph[zx][zy]+=next
                                   graph[i][j]-=next
                                else:
                                    graph[zx][zy] -= next
                                    graph[i][j] += next
    for i in range(n):
        for j in range(c):
            up[i][j]+=graph[i][j]
    return up


def make_before(up):
    temp=[]
    row=len(up)
    col=len(up[0])
    for j in range(col):
        for i in range(row-1,-1,-1):
            if up[i][j]!=-1:
                temp.append(up[i][j])
    return temp

def up_move1(e1):
    # 이제 궁중 부양을 진행 할거임

    up = []
    e = deque(e1)

    #첫번째 공중 부양 할거임
    temp=[]
    t1=[]
    for i in range(n//2):
        t1.append(e.popleft())
    t1.reverse()
    temp.append(t1)
    t1=[]
    for i in range(n//2):
        t1.append(e.popleft())
    temp.append(t1)

    #이제 공중 부양만 하면 된다.
    a1=[]

    for i in range(2):
        t=[]
        for j in range(n//4):
            t.append(temp[i].pop(0))
        a1.append(t)


    for i in a1:
        i.reverse()
    a1.reverse()

    for k in temp:
        a1.extend([k])

    a1=a1
    return a1



while 1:
    if max(e)-min(e)<=k:
        print(time)
        break
    e = first_eat(e)
    e = up_move(e)
    #어항에 있는 물고기 수 조절

    e=delete_fish(e)
    #다시 일렬로 어항을 만듬
    e=make_before(e)
    #다시 공중 부양 작업을 진행 해야함


    e=up_move1(e)
    e=delete_fish(e)
    e=make_before(e)

    time += 1
    if max(e)-min(e)<=k:
        print(time)
        break