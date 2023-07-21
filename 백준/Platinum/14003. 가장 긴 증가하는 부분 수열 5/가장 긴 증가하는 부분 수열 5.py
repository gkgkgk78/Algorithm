import sys

input = sys.stdin.readline
n=int(input().rstrip())
e=list(map(int,input().split()))

#가장 긴 증가 수열 길이를 구하기 위해 체크하는 리스트
dp=[0]*(n+1)
dp[0]=e[0]
index=0

#길이만이 아닌 순서를 구하고자 하는 리스트
total=[-1]*(n)
total[0]=0

def binary(now):
    left=-1
    right=index+1
    #해당 문제는 가장 끝값이 작게 만드는게 유리하다
    while left+1<right:
        mid=(left+right)//2
        if now<=dp[mid]:
            right=mid
        else:
            left=mid
    return right

for i in range(1,n):
    now=e[i]
    if dp[index]<now:
        index+=1
        dp[index]=now
        total[i]=index
    else:
        h=binary(now)
        if h!=-1:
            total[i]=h
            dp[h]=now
last=[-1]*(index+1)
print(index+1)


#내가 구한 길이만큼 이제 나왔을거다
#그 길이에 해당되는 얘부터 찾아야함
# ex
# 4
# 1 4 2 3
#이면은
#0 1 1 2 로 된다
#index 는 2이므로 현재 2에 해당되는 3이 * * 3이되고
#이 3 의 바로전에 가장 증가하는 부분수열인 2 가 되어 * 2 3(index=1)
#그리고 index=0에 해당되는 1 이 되어 1 2 3 이 된다.

for i in range(len(total)-1,-1,-1):
    t=total[i]
    if index==total[i]:
        last[index]=e[i]
        index-=1
print(*last)