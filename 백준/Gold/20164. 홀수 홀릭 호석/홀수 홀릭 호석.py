import sys
from collections import deque

ans_min = sys.maxsize
ans_max = -sys.maxsize
input = sys.stdin.readline
n = str(input().rstrip())


def dfs(now, val):
    global ans_max, ans_min

    if len(now) == 1:
        ans_min = min(ans_min, val)
        ans_max = max(ans_max, val)
        return
    no = val
    # 이제 쪼개야 한다
    if len(now) == 2:
        nex = (int)(now[0]) + (int)(now[1])
        laz = (str)(nex)
        for kk in laz:
            if (int)(kk) % 2 == 1:
                no += 1
        dfs(laz, no)

    else:
        # 이제 쪼갠다
        # 가자가자가자구
        for i in range(len(now) - 2):
            for j in range(i + 1, len(now) - 1):
                for k in range(j + 1, len(now)):
                    no = val
                    first = (int)(now[:j])
                    second = (int)(now[j:k])
                    third = (int)(now[k:])
                    la = first + second + third
                    laz=(str)(la)

                    for kk in laz:
                        if (int)(kk) % 2 == 1:
                            no += 1
                    dfs(laz, no)

vv = 0
for i in n:
    if (int)(i) % 2 == 1:
        vv += 1
dfs(n, vv)
print(ans_min,ans_max)