import sys
input = sys.stdin.readline
n=int(input().rstrip())
arr=[]
for _ in range(n):
    t=list(map(int,input().split()))
    arr.append(t)

sumz=[[0]*(n+1) for _ in range(n+1)]
#합 구하는 과정을 해보자
for i in range(1,n+1):
    for j in range(1,n+1):
        sumz[i][j]=sumz[i-1][j]+sumz[i][j-1]-sumz[i-1][j-1]+arr[i-1][j-1]

answer=-sys.maxsize
for i  in range(n):
    for j in range(n):
        x1, y1 = i, j
        answer=max(answer,arr[i][j])
        for k in range(1,n):
         x2=x1+k
         y2=y1+k
         if x2>=n or y2>=n:
             break
         #정글, 바다, 얼음
         junz=sumz[x2+1][y2+1]-sumz[x1][y2+1]-sumz[x2+1][y1]+sumz[x1][y1]
         answer=max(answer,junz)


print(answer)
