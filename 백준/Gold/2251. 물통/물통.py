import sys,copy
from collections import deque

input=sys.stdin.readline
sys.setrecursionlimit(10**5)

#한 물통이 비거나 , 다른 한 물통이 가득 찰 때까지 물을 붓는다


def bfs(s1,s2):
    q=deque()
    q.append((s1,s2,c))

    total=c
    while q:
        g1,g2,g3=q.popleft()
        if check[g1][g2]==0:
            check[g1][g2]=1
            if g1==0:
                ans.append(g3)

            if g1+g2<=b :#비거나
                q.append((0,g1+g2,g3))
            else :#가득차거나
                q.append((g1+g2-b,b,g3))

            if g1 + g3 <= c:  # 비거나
                q.append((0, g2, g1+g3))
            else:  # 가득차거나
                q.append((g1 + g3 - c, g2, c))

            if g2 + g3 <= c:  # 비거나
                q.append((g1, 0, g2+g3))
            else:  # 가득차거나
                q.append((g2, g2+g3-c, c))

            if g1 + g2 <= a:  # 비거나
                q.append((g1+g2, 0, g3))
            else:  # 가득차거나
                q.append((a, g1+g2-a, g3))

            if g3 + g1 <= a:  # 비거나
                q.append((g1+g3, g2, 0))
            else:  # 가득차거나
                q.append((a, g2, g1+g3-a))

            if g3 + g2 <= b:  # 비거나
                q.append((g1, g2 + g3, 0))
            else:  # 가득차거나
                q.append((g1 , b, g2+g3-b))


a,b,c=map(int,input().split())

check=[[0]*201 for _ in range(201)]
ans=[]
bfs(0,0)
ans.sort()
print(*ans)








