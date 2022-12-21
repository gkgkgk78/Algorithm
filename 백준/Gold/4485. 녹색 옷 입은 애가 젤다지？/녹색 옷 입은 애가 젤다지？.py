import sys,heapq
input=sys.stdin.readline

problem=1
def dijk(graph,t):
    temp=[[sys.maxsize]*t for _ in range(t)]

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    q=[]
    temp[0][0] = graph[0][0]
    heapq.heappush(q,(temp[0][0],0,0))

    while q:
        a1=heapq.heappop(q)
        if a1[1]==t-1 and a1[2]==t-1:
            return temp[a1[1]][a1[2]]

        for i in range(4):
            zx=a1[1]+dx[i]
            zy=a1[2]+dy[i]
            if 0<=zx<t and 0<=zy<t:
                if temp[zx][zy]>a1[0]+graph[zx][zy]:
                    temp[zx][zy]=a1[0]+graph[zx][zy]
                    heapq.heappush(q,(temp[zx][zy],zx,zy))




ans=""
while 1:
    t = int(input().rstrip())
    if t==0:
        break
    graph=[list(map(int,input().split())) for _ in range(t)]
    res=dijk(graph,t)
    ans+="Problem "+str(problem)+": "+str(res)+"\n"
    problem+=1

print(ans)