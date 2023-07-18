import sys
input = sys.stdin.readline

e=list(map(int,input().rstrip()))

if sum(e)%3==0:
    e.sort(reverse=True)
    ss=""
    if e[-1]==0:
        for i in e:
            ss+=str(i)
        print(ss)
    else:
        print(-1)
else:
    print(-1)