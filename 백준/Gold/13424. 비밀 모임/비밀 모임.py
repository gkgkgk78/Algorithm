import sys
import math
from collections import deque
import heapq

input = sys.stdin.readline

t = int(input().rstrip())


def dijk(start, v, graph):
    distance = [sys.maxsize] * (v + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (start, 0))
    while q:
        ver, val = heapq.heappop(q)
        if distance[ver] < val:
            continue
        for vertex, value in graph[ver]:
            nex = value + val
            if distance[vertex] > nex:
                distance[vertex] = nex
                heapq.heappush(q, (vertex, nex))

    return distance


for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a1, a2, a3 = map(int, input().split())
        graph[a1].append((a2, a3))
        graph[a2].append((a1, a3))
    ans = sys.maxsize
    index = -1
    k = int(input().rstrip())
    e = list(map(int, input().split()))
    for i in range(1, v + 1):
        temp = 0
        aa = dijk(i, v, graph)
        for j in e:
            temp += aa[j]
        if temp < ans:
            ans = temp
            index = i
    print(index)