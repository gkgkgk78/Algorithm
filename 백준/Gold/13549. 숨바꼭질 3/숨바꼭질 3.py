import sys
from collections import deque

input = sys.stdin.readline
visit = [sys.maxsize] * (100001)

n, k = map(int, input().split())


def bfs():
    q = deque()
    visit[n] = 0
    q.append((n, 0))

    while q:
        vertex, time = q.popleft()
        if vertex == k:
            print(time)
            return
        dx = [-1, 1]
        for i in range(2):
            z = vertex + dx[i]
            if 0 <= z <= 100000:
                if time + 1 < visit[z]:
                    visit[z] = time + 1
                    q.append((z, time + 1))
        z = vertex * 2
        if 0 <= z <= 100000:
            if time < visit[z]:
                visit[z] = time
                q.appendleft((z, time))


bfs()