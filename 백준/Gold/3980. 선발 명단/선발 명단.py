import sys


input = sys.stdin.readline

ans=-1
def dfs(graph,now,index):
    global ans
    if index==11:
        aa=0
        for i in range(11):
            aa+=graph[i][now[i]]
        ans=max(ans,aa)
        return

    for i in range(11):
        if graph[index][i]!=0:
            if i not in now:
                nn=now.append(i)
                dfs(graph,now,index+1)
                now.pop()


n = int(input().rstrip())
for _ in range(n):
    graph=[]
    for _ in range(11):
        graph.append(list(map(int,input().split())))
    ans=-1
    dfs(graph,[],0)
    print(ans)