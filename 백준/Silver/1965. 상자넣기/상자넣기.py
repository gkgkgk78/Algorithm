import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


a= int(input())
t=list(map(int,input().split())) # 나무 수, 필요한 나무 길이


dp=[]


for i in range (0,a):
    dp.append(0)
    dp[i]=1
    for j in range(0,i):
        if t[j]<t[i] and dp[j]+1 >dp[i]:
            dp[i]=dp[j]+1

print(max(dp))
