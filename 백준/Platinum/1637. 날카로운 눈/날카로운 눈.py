import sys
input = sys.stdin.readline
n=int(input().rstrip())

first=[]
second=[]
last=[]

def find(x):
    count=0
    for l in range(n):
        if x>=first[l]:
            ne = min(last[l], x)
            k=(ne-first[l])//second[l]
            count+=(k+1)
    return count

left=0
right=2147483648

for _ in range(n):
    a1,a2,a3=map(int,input().split())
    first.append(a1)
    second.append(a3)
    last.append(a2)


ans=-1
while left+1<right:
    mid=(left+right)//2
    check=find(mid)

    if check%2==0:
        left=mid
    else:
        right=mid

check=find(right)
if check%2==1:
    be=find(right-1)
    print(right,check-be)
else:
    print("NOTHING")