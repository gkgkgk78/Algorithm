import sys


n=int(input().rstrip())
e=list(map(int,input().split()))
odd=[0]
even=[0]

for i in range(n):
    if i%2==0:
        odd.append(e[i])
    else:
        even.append(e[i])

for i in range(2,n//2+1):
    odd[i]+=odd[i-1]
    even[i]+=even[i-1]

ans=-sys.maxsize

for i in range(n//2+1):
    left=odd[i]
    right=even[-1]-even[i]
    ans=max(left+right,ans)


    left = odd[i]
    right = even[-2] - even[i-1]
    ans = max(left + right, ans)

print(ans)