import sys

input = sys.stdin.readline
n=int(input().rstrip())
a1=int(input().rstrip())
a=list(map(int,input().split()))
a2=int(input().rstrip())
b=list(map(int,input().split()))

adda=[]
addb=[]

for i in range(a1):
    sumz=0
    for j in range(i,a1):
        sumz+=a[j]
        adda.append(sumz)
for i in range(a2):
    sumz=0
    for j in range(i,a2):
        sumz+=b[j]
        addb.append(sumz)
addb.sort()
tt=len(addb)

#이제 구하도록 하자.

def find_lower(i):
    left=-1
    right=tt
    g1=addb
    #이렇게 해서 시작을 하도록 하자
    while left+1<right:
        mid=(left+right)//2
        if addb[mid]>=i:
            right=mid
        else:
            left=mid
    return right


def find_uppper(i):
    left = -1
    right = tt 

    # 이렇게 해서 시작을 하도록 하자
    while left + 1 < right:
        mid = (left + right) // 2
        if addb[mid] > i:
            right = mid
        else:
            left = mid
    return left

cnt=0
for i in adda:
    now=n-i

    lower=find_lower(now)
    upper=find_uppper(now)
    cnt+=(upper-lower+1)
print(cnt)