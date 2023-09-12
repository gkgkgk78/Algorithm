import sys
input = sys.stdin.readline
n,m,l,k=map(int,input().split())
star=[]
for _ in range(k):
    a1,a2=map(int,input().split())
    star.append((a1,a2))

ans=0
for i in range(k):
    for j in range(k):
        temp=0
        for e in range(k):
            if star[i][0]<=star[e][0] and star[i][0]+l>=star[e][0] and star[j][1]<=star[e][1] and star[j][1]+l>=star[e][1]:
                temp+=1
        ans=max(ans,temp)

print(k-ans)