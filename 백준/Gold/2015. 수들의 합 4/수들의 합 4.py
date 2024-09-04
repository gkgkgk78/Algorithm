import sys
input = sys.stdin.readline

n,k=map(int,input().split())
e=list(map(int,input().split()))
data=[0]*(n)
data[0]=e[0]
test=dict()
test[e[0]]=1
answer=0
if e[0]==k:
    answer+=1
for i in range(1,n):
    data[i]=data[i-1]+e[i]
    if data[i]==k:
        answer+=1
    now=data[i]-k
    if now in test:
        answer+=test[now]
    if data[i] in test:
        test[data[i]]+=1
    else:
        test[data[i]]=1
print(answer)