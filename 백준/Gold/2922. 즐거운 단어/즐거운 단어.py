import sys
from collections import deque

input = sys.stdin.readline
mo = ["A", "E", "I", "O", "U"]
ja = ["B", "C", "D", "F", "G", "H", "J", "K", "M", "L",
      "N", "P", "Q", "R", "S", "T", "V"
    , "W", "X", "Y", "Z"]
e = list(map(str, input().rstrip()))
ch = e.count("_")


def check(no, go):
    for i in range(len(no) - 2):
        if i + 2 < len(no):
            if no[i] in go and no[i + 1] in go and no[i + 2] in go:
                return 0
    return 1


ans = 0


def dfs(now, co, cnt):
    global ans
    if co == 0:
        if "L" not in now:
            return
        a1 = check(now, mo)
        if a1 == 0 :
            return
        a2 = check(now, ja)
        if a2 == 0 :
            return
        ans += cnt
        return
    ind = -1
    for i in range(len(now)):
        if now[i] == "_":
            ind = i
            # 이제 넣을 거야
    # 모음 시작
    now[ind] = "A"
    dfs(now, co - 1, cnt * 5)
    # 자음 시작
    now[ind] = "C"
    dfs(now, co - 1, cnt * 20)
    # L
    now[ind] = "L"
    dfs(now, co - 1, cnt)

    now[ind] = "_"


dfs(e, ch, 1)
print(ans)