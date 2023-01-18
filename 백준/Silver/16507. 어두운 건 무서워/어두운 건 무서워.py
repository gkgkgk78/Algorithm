import sys
input = sys.stdin.readline
r,c,q=map(int,input().split())
graph=[]

for l in range(r):
    graph.append(list(map(int,input().split())))
temp=[[0]*(c+1)for _ in range(r+1)]


for i in range(1,r+1):
    for j in range(1,c+1):
        temp[i][j]=graph[i-1][j-1]+temp[i-1][j]+temp[i][j-1]-temp[i-1][j-1]


for _ in range(q):
    a1,a2,a3,a4=map(int,input().split())
    a1-=1
    a2-=1
    a3-=1
    a4-=1
    now=temp[a3+1][a4+1]-temp[a1][a4+1]-temp[a3+1][a2]+temp[a1][a2]
    tt = (a3 - a1 + 1) * (a4 - a2 + 1)
    print(now//tt)