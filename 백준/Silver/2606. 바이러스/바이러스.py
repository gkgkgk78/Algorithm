import sys
#sys.stdin = open("input.txt")

t1=0
def DFS(x):
    global t1
    if len(stack)==0:
      return
    else:
      for i in range(0,n):
        if check[x][i]==1 and visit[i]==0:
          visit[i]=1
          stack.append(i)
          #print(x,i)
          t1=t1+1
          DFS(i)
      stack.pop()







n=int(input())
m=int(input())
map=[]
for i in range (m):
  map.append(list(input().split()))
check = [[0] * n for _ in range(n)]
visit = [0 for _ in range(n)]

for i in range(m):
  i1=int(map[i][0])-1
  i2=int(map[i][1])-1
  #print(i1,i2)
  check[i1][i2]=1
  check[i2][i1] = 1

stack=[]
visit[0]=1
stack.append(0)
DFS(0)
print(t1)
