import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

start = ""
last = []
index = dict()
revers = dict()
for i in range(n):
    now = str(input().rstrip())
    last.append(now)
    if i == 0:
        start = now
    index[now] = i + 1
    revers[i + 1] = now

parent = [0] * (n + 1)
visit = dict()
parent[1] = 1


def bfs():
    visit[start] = 1
    q = deque()
    q.append(start)
    while q:
        now1 = q.popleft()
        for j in range(k):
            now = now1
            ne = ""
            if now[j] == "1":
                ne = "0"
            else:
                ne = "1"
            now = now1[:j] + ne + now1[j + 1:]
            if now in visit or now not in index:
                continue
            beforeIndex = index[now1]
            nextIndex = index[now]
            parent[nextIndex] = beforeIndex
            visit[now] = 1
            q.append(now)
bfs()
z = int(input().rstrip())
def makeRoute(ind):
    la = [ind]
    now = ind
    while 1:
        now = parent[now]
        la.append(now)
        if now == 1:
            break
    return la


for i in range(z):
    now = int(input().rstrip())
    value = revers[now]
    if value not in visit:
        print(-1)
    else:
        no=makeRoute(now)
        no.reverse()
        print(*no)