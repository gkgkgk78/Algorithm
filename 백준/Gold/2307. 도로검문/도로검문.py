import sys
import heapq

input = sys.stdin.readline
e = []
n, m = map(int, input().split())
for _ in range(m):
    a1, a2, a3 = map(int, input().split())
    e.append([a1, a2, a3])
graph = [[] for _ in range(n + 1)]

for a1, a2, a3 in e:
    graph[a1].append((a2, a3))
    graph[a2].append((a1, a3))

temp = [[] for _ in range(n + 1)]


def dijk():
    q = []
    distance = [sys.maxsize] * (n + 1)
    distance[1] = 0
    heapq.heappush(q, (0, 1, 1))

    while q:
        value, vertex, vertex1 = heapq.heappop(q)
        if distance[vertex] < value:
            continue
        for ver, val in graph[vertex]:
            if distance[ver] > value + val:
                distance[ver] = value + val
                heapq.heappush(q, (distance[ver], ver, vertex))
                temp[ver]=[vertex]

    return distance


first = dijk()

# 이제 부터 하나의 도로를 막음으로써 지연시키는 최대 시간 정수로 출력 하자
ans = -sys.maxsize


def dijk1(s1, s2):
    q = []
    distance = [sys.maxsize] * (n + 1)
    distance[1] = 0
    heapq.heappush(q, (0, 1))

    while q:
        value, vertex = heapq.heappop(q)
        if distance[vertex] < value:
            continue

        for ver, val in graph[vertex]:
            if vertex == s1 and ver == s2:
                continue
            if vertex == s2 and ver == s1:
                continue
            if distance[ver] > value + val:
                distance[ver] = value + val
                heapq.heappush(q, (distance[ver], ver))

    return distance
route=[]
curr=n
route.append(n)
while curr!=1:
    route.append(temp[curr][0])
    curr=temp[curr][0]

for i in range(len(route)-1):
    a1=route[i]
    a2=route[i+1]
    second = dijk1(a1, a2)
    next = -1
    if second[n] == sys.maxsize:
        next = sys.maxsize
    else:
        next = second[n] - first[n]
    ans = max(ans, next)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)