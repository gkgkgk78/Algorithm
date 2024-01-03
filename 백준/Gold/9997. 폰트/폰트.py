import sys
input = sys.stdin.readline
n = int(input().rstrip())

total = [0] * (n)
for i in range(n):
    e = str(input().rstrip())
    now = 0
    for k in e:
        temp = 1 << ord(k) - 97
        now |= temp
    total[i] = now
answer = 0
last = (1 << 26) - 1
def dfs(index, now):
    global answer
    if index == n:
        if now == last:
            answer += 1
        return
    dfs(index + 1, now)
    dfs(index + 1, now | total[index])
dfs(0, 0)
print(answer)