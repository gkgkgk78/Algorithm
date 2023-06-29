import sys

input = sys.stdin.readline

n=int(input().rstrip())
e=[]
for _ in range(n):
    a1,a2=map(int,input().split())
    e.append((a1,a2))
e.sort()

ans=0
left=e[0][0]
right=e[0][1]
ans+=(right-left)

for l in range(1,n):
    a1,a2=e[l]
    if a1>=left and a2<=right:
        continue
    if a1>right:
        left=a1
        right=a2
        ans += (right - left)
        continue
    if a2>=right:
        ans+=(a2-right)
        right=a2

print(ans)