import sys


input = sys.stdin.readline


n=int(input().rstrip())

visit=[0]*(n+1)
graph=[[] for _ in range(n+1)]

total=[[0]*2 for _ in range(n+1)]
route=[[[], []] for i in range(n + 1)]
weight=list(map(int,input().split()))

root=[]


#0 나포함 1: 나포함하지 않음


def dfs(vertex,visit,graph,total,weight):

    route[vertex][0].append(vertex)
    for i in graph[vertex]:
        if visit[i]==1:
            continue
        visit[i]=1
        dfs(i,visit,graph,total,weight)
        visit[i]=0
        total[vertex][0]+=total[i][1]
        for l in route[i][1]:
            route[vertex][0].append(l)
        total[vertex][1]+=max(total[i][0],total[i][1])

        if total[i][0]>total[i][1]:
            for l in route[i][0]:
                route[vertex][1].append(l)
        else:
            for l in route[i][1]:
                route[vertex][1].append(l)



for _ in range(n-1):
    a1,a2=map(int,input().split())
    graph[a1].append(a2)
    graph[a2].append(a1)





for i in range(1,n+1):
    total[i][0] = weight[i - 1]
    if len(graph[i])==1:
        root.append(i)

visit[root[0]]=1
now=root[0]
dfs(root[0],visit,graph,total,weight)




if total[now][0]>total[now][1]:
    print(total[now][0])
    t=route[now][0]
    t.sort()
    print(*t)

else:
    print(total[now][1])
    t = route[now][1]
    t.sort()
    print(*t)