from itertools import permutations,combinations,product
import sys
input = sys.stdin.readline
def dfs(cnt):
    global ans
    if cnt==15:
        if w.count(0)==6 and d.count(0)==6 and l.count(0)==6:
            ans=1
        return
    #승패
    a1,a2=game[cnt]
    if w[a1]>0 and l[a2]>0:
        w[a1]-=1
        l[a2]-=1
        dfs(cnt+1)
        w[a1]+=1
        l[a2]+=1
    #패승
    if l[a1]>0 and w[a2]>0:
        l[a1]-=1
        w[a2]-=1
        dfs(cnt+1)
        l[a1]+=1
        w[a2]+=1

    #무무
    if d[a1]>0 and d[a2]>0:
        d[a1]-=1
        d[a2]-=1
        dfs(cnt+1)
        d[a1]+=1
        d[a2]+=1


game = list(combinations(range(6), 2))
result = []
for i in range(4):
    a = list(map(int, input().split()))
    w, l, d = [], [], []
    for j in range(18):
        if j % 3 == 0: w.append(a[j])
        elif j % 3 == 1: d.append(a[j])
        elif j % 3 == 2: l.append(a[j])
    ans = 0
    dfs(0)
    result.append(ans)
print(*result)