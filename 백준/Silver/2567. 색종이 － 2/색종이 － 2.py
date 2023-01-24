import sys
input = sys.stdin.readline

n=int(input().rstrip())
graph=[[0]*(101) for _ in range(101)]

for _ in range(n):
    a1,a2=map(int,input().split())

    for i in range(a1,a1+10):
        for j in range(a2,a2+10):
            graph[i][j]=1


answer=0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(101):
    for j in range(101):
        if graph[i][j]==1:
            for l in range(4):
                zx = dx[l] + i
                zy = dy[l] + j
                if 0 <= zx <= 100 and 0 <= zy <= 100:
                    if graph[zx][zy] == 0:
                        answer+=1
print(answer)