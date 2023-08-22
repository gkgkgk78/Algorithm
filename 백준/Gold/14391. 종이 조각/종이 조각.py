import sys

input = sys.stdin.readline

n, m = map(int, input().split())
visit = [[-1] * (m) for _ in range(n)]
graph = []
for _ in range(n):
    e = list(map(int, input().rstrip()))
    graph.append(e)
ans = -sys.maxsize



for i in range(1<<n*m):
    result=0
    #가로합 계산
    for j in range(n):
        temp=0
        for k in range(m):
            idx=j*m+k
            if i&(1<<idx)!=0:
                temp=temp*10+(graph[j][k])
            else:
                result+=temp
                temp=0
        result+=temp
    for j in range(m):
        temp=0
        for k in range(n):
            idx=k*m+j
            if i&(1<<idx)==0:
                temp=temp*10+(graph[k][j])
            else:
                result+=(int)(temp)
                temp=0
        result += temp

    ans=max(ans,result)
print(ans)