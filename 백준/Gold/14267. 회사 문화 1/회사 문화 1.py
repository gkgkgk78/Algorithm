import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m=map(int,input().split())
dp=[0]*(n+1)
visit=[0]*(n+1)
graph=[[]for _ in range(n+1)]
e=list(map(int,input().split()))
for i in range(1,len(e)):
    graph[e[i]].append(i+1)
temp=[0]*(n+1)
for _ in range(m):
    a1,a2=map(int,input().split())
    temp[a1]+=a2
total=[0]*(n+1)
def dfs(v,go):
    visit[v]=1
    total[v]=temp[v]+go
    for i in graph[v]:
        if visit[i]==1:
            continue
        dfs(i,total[v])

dfs(1,0)
print(*total[1:])