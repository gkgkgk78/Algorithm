import sys


a=[""]
b=[""]
a.extend(list(map(str,input().rstrip())))

b.extend(list(map(str,input().rstrip())))

dp=[[0]*(len(a))for _ in range(len(b))]

for i in range(len(b)):
    for j in range(len(a)):
        if i==0 or j==0:
            dp[i][j]=0
        else:
            if a[j]==b[i]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j] =max(dp[i-1][j],dp[i][j-1])
ans=-sys.maxsize
def dfs(x,y,now):
    global ans,a

    if dp[x][y]==0:
        return -1
    a1=dp[x - 1][y]
    a2=dp[x][y - 1]
    if a1==dp[x][y] or a2==dp[x][y]:
        if a1 == dp[x][y]:
            a=dfs(x-1,y,now)
            if a==-1:
                return -1
        if a2==dp[x][y]:
            a=dfs(x,y-1,now)
            if a==-1:
                return -1
    else:
        now.append(a[y])
        a=dfs(x - 1, y-1, now)
        if a==-1:
            return -1
        now.pop()




for i in dp:
    ans=max(ans,max(i))
if ans==0:
    print(ans)
else:
    print(ans)
    now=[]
    dfs(len(dp)-1,len(dp[0])-1,now)
    
    now.reverse()
    print("".join(map(str,now)))