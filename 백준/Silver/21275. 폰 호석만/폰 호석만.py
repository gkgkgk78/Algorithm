import sys

input = sys.stdin.readline

a1,a2=map(str,input().split())

low1=2
low2=2
for i in a1:
    if i.isalpha():
        low1=max(low1,ord(i)-97+10+1)
    if i.isdigit():
        low1=max(low1,(int)(i)+1)
for i in a2:
    if i.isalpha():
        low2=max(low2,ord(i)-97+10+1)
    if i.isdigit():
        low2=max(low2,(int)(i)+1)

ma=2**63
cnt=0

x=-1
a=-1
b=-1
for i in range(low1,37):
    for j in range(low2,37):
        f1=(int)(a1,i)
        f2=(int)(a2,j)
        if f1>=ma or f2 >=ma:
            continue

        if f1==f2 and i!=j:
            cnt+=1
            x=f1
            a=i
            b=j

if cnt==1:
    print(x,a,b)
elif cnt==0:
    print("Impossible")
else:
    print("Multiple")