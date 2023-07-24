import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, s = map(int, input().split())

left = dict()
e = list(map(int, input().split()))
ee = e[:n // 2]


def dfs(index, sumz):
    if index == n // 2+1:
        if sumz not in left:
            left[sumz] = 0
        left[sumz] += 1
        return
    dfs(index + 1, sumz)
    dfs(index + 1, sumz + e[index])


ans = 0


def dfsr(index, sumz):
    global ans
    if index == n:
        ne = s - sumz
        if ne in left:
            ans += left[ne]
        return
    dfsr(index + 1, sumz)
    dfsr(index + 1, sumz + e[index])

dfs(0, 0)
dfsr(n // 2 + 1, 0)
if s==0:
    ans-=1
print(ans)