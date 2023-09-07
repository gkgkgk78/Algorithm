import sys

input = sys.stdin.readline
n = int(input().rstrip())
e = []

for _ in range(n):
    e.append(str(input().rstrip()))

left = 0
right = n - 1


ans = ""
while left < right:

    a1 = ord(e[left])
    a2 = ord(e[right])
    if left + 1 == right:
        if a1 < a2:
            ans += e[left]
            ans += e[right]
        elif a2 <= a1:
            ans += e[right]
            ans += e[left]
        break

    if a1 < a2:
        ans += e[left]
        left += 1
    elif a2 < a1:
        ans += e[right]
        right -= 1
    else:

        n1=left+1
        n2=right-1
        while n1<=n2:
            if n1==n2 or n1==n2-1:
                ans += e[right]
                right -= 1
                break
            if e[n1]<e[n2]:
                ans += e[left]
                left += 1
                break
            elif e[n2] < e[n1]:
                ans += e[right]
                right -= 1
                break
            n1+=1
            n2-=1

if len(e)==1:
    ans=str(e[0])
total=[]
temp=""
for i in ans:
    temp+=i
    if len(temp)==80:
        total.append(temp)
        temp=""
total.append(temp)
for i in total:
    print(i)