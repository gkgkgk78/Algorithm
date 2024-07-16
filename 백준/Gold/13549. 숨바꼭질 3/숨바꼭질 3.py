import sys
from collections import deque

input = sys.stdin.readline

visit = [-1] * (100001)
q = deque()
n, m = map(int, input().split())

time = 0
q.append((n))
visit[n] = 0
while q:
    vertex = q.popleft()
    if vertex == m:
        time = visit[vertex]
        break
    if vertex * 2 <= 100000 and visit[vertex * 2] == -1:
        q.appendleft((vertex * 2))
        visit[vertex * 2] = visit[vertex]
    if 0 <= vertex - 1 <= 100000 and visit[vertex - 1] == -1:
        q.append((vertex - 1))
        visit[vertex - 1] = visit[vertex] + 1
    if 0 <= vertex + 1 <= 100000 and visit[vertex + 1] == -1:
        q.append((vertex + 1))
        visit[vertex + 1] = visit[vertex] + 1
print(time)