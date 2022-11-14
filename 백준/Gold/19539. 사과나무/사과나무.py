import sys
input = sys.stdin.readline

n=int(input().rstrip())
total=list(map(int,input().split()))
sumz=sum(total)

if(sumz%3!=0):
    print("NO")
else:
    first=sumz//3

    for i in total:
        first-=i//2
    if first <=0:
        print("YES")
    else:
        print("NO")