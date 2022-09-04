import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


a= int(input())
t=list(map(int,input().split())) # 나무 수, 필요한 나무 길이


dp=[]
dp1=[]


for i in range (0,a):
    dp.append(0)
    dp1.append(0)
    dp[i]=1
    dp1[i]=t[i]
    for j in range(0,i):
        if t[j]<t[i] :

            dp1[i]=max(dp1[i],dp1[j]+t[i])


print((max(dp1)))