import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

t = int(input().rstrip())

visit = []
done = dict()


def dfs(vertex, e):
    global visit, cycle, ans

    visit[vertex] = 1
    cycle.append(vertex)
    next = e[vertex]

    if visit[next] == 1:
        if next in cycle:
            ans -= (len(cycle) - cycle.index(next))

    else:
        dfs(next, e)


for _ in range(t):
    n = int(input().rstrip())
    done = dict()
    visit = [0] * (n + 1)
    e = [0] + list(map(int, input().split()))
    ans = n
    for k in range(1, n + 1):
        if visit[k] == 0:
            cycle = []
            dfs(k, e)
    print(ans)