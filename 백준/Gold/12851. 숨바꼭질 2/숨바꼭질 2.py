from collections import deque
 
N, K = map(int, input().split())
MAX_SIZE = 100001
MAP = [[MAX_SIZE, 0] for _ in range(MAX_SIZE)]
 
q = deque()
q.append(N)
MAP[N][0] = 0
MAP[N][1] = 1
 
while q:
    x = q.popleft()
    for nx in [x*2, x+1, x-1]:
        if 0 <= nx < MAX_SIZE:
            if MAP[nx][0] == MAX_SIZE:
                q.append(nx)
                MAP[nx][0] = MAP[x][0] + 1
                MAP[nx][1] = MAP[x][1]
            elif MAP[nx][0] == MAP[x][0]+1:
                MAP[nx][1] += MAP[x][1]
 
print(MAP[K][0])
print(MAP[K][1])