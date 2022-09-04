from collections import deque
import sys
import sys
#sys.stdin = open("input.txt")

n,m,k1=(map(int,input().split()))
map=[]
for i in range (k1):
  map.append(list(input().split()))
check = [[0] * m for _ in range(n)]
check1 = [[0] * m for _ in range(n)]
for i in range (k1):
  j1=int(map[i][0])
  j2 = int(map[i][1])

  check[j1-1][j2-1]=1

#print(check1)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def DFS(x,y):
  t=1
  q = deque()
  q.append([x, y])
  check1[x][y] = 1
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx,ny=dx[i]+x,dy[i]+y
      if 0<=nx<n and 0<=ny<m and check1[nx][ny]==0 and check[nx][ny]==1:
        #print(nx,ny)
        q.append([nx,ny])
        check1[nx][ny]=check1[x][y]+1
        t+=1
  return t

uo=0
for i in range(n):
  for j in range(m):
    if 0 <= i < n and 0 <= j < m and check1[i][j] == 0 and check[i][j] == 1:
      ah=DFS(i,j)
      #print(ah)
      if ah>uo:
        uo=ah

print(uo)
