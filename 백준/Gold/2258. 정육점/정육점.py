import sys

input = sys.stdin.readline

n, m = map(int, input().split())


total=[]
for _ in range(n):
    weight,price=map(int,input().split())
    total.append((weight,price))

total=sorted(total,key=lambda x:(x[1],-x[0]))


sumz=0
ans=sys.maxsize
i=0
before=-1
count=0
while i<len(total):
    weight,price=total[i]
    sumz+=weight

    if before==price:
        before=price
        count+=1

        if sumz>=m:
            ans = min(ans, price*count)

    else:
        before=price
        count=1
        if sumz >= m:
            ans = min(ans, price)
    i+=1

if ans==sys.maxsize:
    print(-1)
else:
    print(ans)