n = int(input())

num=list(map(int,input().split()))
err=0
sum=0
for i in range(n):
    d=num[i]
    err=0
    for j in range(2,d+1):
        if d%j==0:
            err=err+1

    if err==1:
        sum=sum+1

print(sum)