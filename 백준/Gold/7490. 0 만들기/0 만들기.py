import sys
input = sys.stdin.readline
t = int(input().rstrip())


# 이제 결과가 0이 되는 모든 수식을 만들어 보도록 하자


def dfs(n, cnt, now):
    if cnt == n:
        #이제 계산 해보도록 하자
        ops=[]
        number=[]
        temp=""
        for i in now:
            if i =="+"or i=="-":
                number.append((int)(temp))
                temp=""
                ops.append(i)
            else:
                if i!=" ":
                    temp+=i
        if len(temp)>0:
            number.append((int)(temp))
        nn=number.pop(0)
        if now=="1+2+3":
            now="1+2+3"
        for i in ops:
            ne=number.pop(0)
            if i=="+":
                nn=nn+ne
            else:
                nn=nn-ne

        if nn==0:
            print(now)

        return

    dfs(n, cnt + 1, now + " "+ (str)(cnt + 1) )
    dfs(n, cnt + 1, now +"+"+ (str)(cnt + 1))
    dfs(n, cnt + 1, now + "-"+ (str)(cnt + 1) )


for _ in range(t):
    n = int(input().rstrip())
    # 최대 가능한 수 파악 해보도록 하자
    # 이제 문자열 추가 해보도록 하자
    dfs(n, 1, "1")

    print()