import sys
from collections import deque
input = sys.stdin.readline
n, t, g = map(int, input().split())
visit = dict()

q = deque()


def bfs():
    if n == g:
        return 0
    q.append((n, 0))  # 현재 수, 누른 횟수
    while q:
        now, co = q.popleft()
        if co > t:
            continue
        if now == g:
            return co
        if now + 1 <= 99999:
            if co + 1 <= t:
                if now + 1 not in visit:
                    visit[now + 1] = 1
                    q.append((now + 1, co + 1))
        if now * 2 <= 99999:
            nex = (str)(now * 2)

            if (int)(nex[0]) - 1 >= 0:
                aa = (int)(nex[0]) - 1
                nex = (str)(aa) + nex[1:]
            nex = (int)(nex)
            if co + 1 <= t and nex not in visit:
                visit[nex] = 1
                q.append((nex, co + 1))
    return "ANG"


ee = bfs()
print(ee)