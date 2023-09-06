import sys

input = sys.stdin.readline


n=int(input().rstrip())
e=list(map(int,input().split()))
e.sort()
ans=[]
an=sys.maxsize
for i in range(n-2):
    now=e[i]
    left=i+1
    right=n-1
    while left<right:
        sumz=e[i]+e[left]+e[right]
        if abs(sumz) < an:
            ans=[e[i],e[left],e[right]]
            an=abs(sumz)
        if sumz==0:
          print(e[i],e[left],e[right])
          sys.exit(0)
        elif sumz<0:
          left+=1
        else:
          right-=1
print(*ans)