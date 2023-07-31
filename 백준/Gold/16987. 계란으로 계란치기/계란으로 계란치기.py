import sys

input = sys.stdin.readline
n = int(input().rstrip())

e = []
for _ in range(n):
    a1, a2 = map(int, input().split())
    e.append([a1, a2])
index = 0
ans = -sys.maxsize


def dfs(index, e):
    global ans
    if index == n:
        count = 0
        for a1, a2 in e:
            if a1 <= 0:
                count += 1

        ans = max(ans, count)
        return
    # 이제 손에 들고 있는 계란으로 깨지ㅣ 않은 다른 계란 중에서 하나를 친다
    n1, n2 = e[index]
    t = 0
    if n1 <= 0:  # 이미 깨진 계란이라면
        dfs(index + 1, e)
    else:
        # 깨지지 않은 계란 이라면
        for i in range(n):
            if i == index:
                continue
            if e[i][0] > 0:  # 깨지지 않은 계란이 존재시
                t1, t2 = e[index]
                t3, t4 = e[i]
                can, weight = e[i]
                t += 1
                # 계란 깨기 시작
                t1 -= weight
                can -= t2
                # 이제 이렇게 해서 dfs 하면됨
                e[index] = [t1, t2]
                e[i] = [can, weight]
                dfs(index + 1, e)
                e[index] = [n1, n2]
                e[i] = [t3, t4]
        if t == 0:
            dfs(index + 1, e)


dfs(0, e)
print(ans)