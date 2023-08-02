import sys
from collections import deque

input = sys.stdin.readline


def bfs(vertex, visit, find, flag):
    visit[vertex] = flag
    q = deque()
    q.append(vertex)
    while q:
        a1 = q.popleft()
        for i in graph[a1]:
            if visit[i] == 0 and find[i] == flag:
                visit[i] = flag
                q.append(i)

def check(go,visit,flag):
    #방문을 했으면 되는 거지
    for i in go:
        if visit[i]==flag:
            continue
        else:
            return -1
    return 1
ans=sys.maxsize
def comb(start, cnt, last, first):
    global ans
    if cnt == last:

        find = [0] * (n + 1)
        second = []  # 이제 안들어 있는 수를 구하면 됨
        for i in range(1, n + 1):
            second.append(i)
        second = list(set(second) - set(first))
        for i in first:
            find[i] = 1
        for i in second:
            find[i] = 2

        # 이제 bfs 를 돌면서 파악을 해보도록 하자
        visit = [0] * (n + 1)

        bfs(first[0], visit, find, 1)
        bfs(second[0], visit, find, 2)
        t1=check(first,visit,1)
        t2=check(second,visit,2)
        if t1==-1 or t2==-1:
            return
        temp=0
        temp1=0
        for i in first:
            temp+=e[i]
        for i in second:
            temp1+=e[i]
        ans=min(ans,abs(temp1-temp))
        return
    for i in range(start, n + 1):
        first[cnt] = i
        comb(i + 1, cnt + 1, last, first)


# 조합으로 1~n-1까지 해서 모든 경우의 수 구한후

n = int(input().rstrip())
e = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    a1 = list(map(int, input().split()))
    for j in range(1, len(a1)):
        graph[i].append(a1[j])

# 구한 상태에서 bfs로 해서 인접한 구역 탐지 하도록 하자

for i in range(1, n):
    # 조합의 수를 구해보도록 하자
    first = [0] * (i)
    comb(1, 0, i, first)
if ans==sys.maxsize:
    print(-1)
else:
    print(ans)