import sys
input = sys.stdin.readline
def check(ne):
    start = 2

    while 1:
        if start > len(ne):
            break
        ind = 0
        while 1:
            if ind + start > len(ne):
                break
            now = ne[ind:ind + start]
            left = now[:len(now) // 2]
            right = now[len(now) // 2:]
            if left == right:
                return 0
            ind += 1
        start += 2
    return 1

n = int(input().rstrip())
def dfs(now):
    if len(now) == n:
        print(now)
        sys.exit(0)
    dd = ["1", "2", "3"]
    for i in dd:
        ne = now + i
        c = check(ne)
        if c == 1:
            dfs(ne)
dfs("1")