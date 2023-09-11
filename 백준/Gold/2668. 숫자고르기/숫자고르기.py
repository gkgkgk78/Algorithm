import sys

input = sys.stdin.readline

n = int(input().rstrip())
first = [0 for _ in range(n + 1)]

second = []

for i in range(1, n + 1):
    first[i] = (int(input().rstrip()))
# print(first)
#
cou = 0
do = []
for i in range(1, n + 1):
    if first[i] == i:
        do.append(i)
ans = -sys.maxsize
last = []

visit = [0] * (n + 1)

def dfs(vertex, visit1, visit2):
    global ans, last,visit

    if visit1[vertex] == 1:
        # 이제 확인을 해봐야지
        if visit1 == visit2:
            for i in range(len(visit1)):
                if visit1[i]==1:
                    visit[i]=1
        return

    now = first[vertex]
    visit1[vertex] = 1
    if visit2[now] == 0:
        visit2[now] = 1
        dfs(now, visit1, visit2)


for i in range(1, n + 1):
    if visit[i]==0:
        visit1 = [0] * (n + 1)
        visit2 = [0] * (n + 1)
        dfs(i, visit1, visit2)
ans=0
last=[]
for i in range(1,len(visit)):
    if visit[i]==1:
        ans+=1
        last.append(i)
print(ans)
for i in last:
    print(i)