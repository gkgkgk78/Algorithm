import sys
from collections import deque
input=sys.stdin.readline
n=int(input().rstrip())
m=int(input().rstrip())
indegree=[0 for _ in range(n+1)]

find=[[0] * (n + 1) for _ in range(n + 1)]

road=[[] for _ in range(n + 1)]

#전체 입력을 받는 과정을 의미를 함
for _ in range(m):
    a1,a2,a3=map(int,input().split())
    indegree[a1]+=1
    road[a2].append((a1,a3))


basic=dict()
q=deque()
for l in range(1,n+1):
    if indegree[l]==0:
        q.append(l)
        basic[l]=0


while(len(q)>0):
    a1=q.popleft()
    for i1,i2 in road[a1]:#도착 지점 횟수
        indegree[i1]-=1
        if indegree[i1]==0:
            if i2==6:
                i2=i2
            q.append(i1)
        if a1 in basic:
            find[i1][a1] += i2
        else:
            for i in range(1, n + 1):
                find[i1][i] += find[a1][i] * i2




for i in range(1,n+1):
    if find[n][i]>0:
        print(str(i)+" "+str(find[n][i]))