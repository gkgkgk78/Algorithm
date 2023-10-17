import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())
jewrly = dict()
cc=0
for _ in range(k):
    a = int(input().rstrip())
    jewrly[a]=cc
    cc+=1
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a1, a2, a3 = map(int, input().split())
    graph[a1].append((a2, a3))
    graph[a2].append((a1, a3))
visit = [[0] * (1 << 14) for _ in range(n + 1)]

ans = -sys.maxsize


def bfs():
    global ans
    q = deque()
    visit[1][0] = 1
    # 이제 방문을 시작 해야 하는데
    q.append((1, 0, 0))  # 시작점 주운개수 보석현황
    if 1 in jewrly:
        ne=jewrly[1]
        visit[1][1 << ne] = 1
        q.append((1, 1, 1 << ne))

    while q:
        vertex, cnt, value = q.popleft()

        if vertex == 1:
            ans = max(ans, cnt)
        for ver, val in graph[vertex]:
            # 보석 가지고 가지 않을수도 있다
            if cnt <= val and visit[ver][value] == 0:
                visit[ver][value] = 1
                q.append((ver, cnt, value))
            if ver in jewrly:
                check=cnt
                ne=jewrly[ver]
                if (value>>(ne))&1==0:
                    check+=1
                nex = (value) | (1 << ne)

                # 보석 가지고 갈수도 있고
                if cnt <= val and visit[ver][nex] == 0:
                    visit[ver][nex] = 1
                    q.append((ver, check, nex))
bfs()
print(ans)