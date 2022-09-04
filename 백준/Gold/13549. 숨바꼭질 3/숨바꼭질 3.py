from collections import deque
import sys
#sys.stdin = open("input.txt")
N, K = map(int, input().split())
MAX_SIZE = 100001
MAP = [[-1, 0] for _ in range(MAX_SIZE)]
MAP1 = [-1, 0]*(10)

q = deque()
q.append(N)
MAP[N][0] = 0#여기에는 걸린 시간의 수를 저장하는것을 의미한다
MAP[N][1] = 1#여기에는 도달했던 경우의수를 저장한다

while q:
    x = q.popleft()

    if x==K:
        break
    for nx in [ 2*x]:
        if 0 <= nx < MAX_SIZE:
            if MAP[nx][0] == -1:
                q.appendleft(nx)
                MAP[nx][0] = MAP[x][0]
                MAP[nx][1] = MAP[x][1]

    for nx in [ x + 1, x - 1]:
        if 0 <= nx < MAX_SIZE:
            if MAP[nx][0] == -1:
                q.append(nx)
                MAP[nx][0] = MAP[x][0]+1
                MAP[nx][1] = MAP[x][1]


print(MAP[K][0])
#print(MAP[K][1])