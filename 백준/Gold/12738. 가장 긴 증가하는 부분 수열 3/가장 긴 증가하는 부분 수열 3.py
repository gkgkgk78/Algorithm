import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


a= int(input())
t=list(map(int,input().split())) # 나무 수, 필요한 나무 길이

dp=[]
dp1=[]
dp1.append(t[0])


def chch(target,start,end):

    while start<=end:
        mid=(start+end)//2

        if dp1[mid]>= target:
            end=mid-1
        else:
            start=mid+1
    return start





for i in range(1,a):
    gg=len(dp1)
    if t[i]>dp1[gg-1]:
        dp1.append(t[i])
    else:
        g=chch(t[i],0,gg-1)
        dp1[g]=t[i]
print(len(dp1))