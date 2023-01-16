import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
answer=-sys.maxsize
def tt(minus,plus,ll):
    global answer
    sum=[]
    if a[0]==minus:
        sum.append(-1)
    else:
        sum.append(1)
    for i in range(1,n):
        now=0
        if ll[i]==minus:
            now=-1
        else:
            now=1
        sum.append(max(0,sum[i-1])+now)
    answer=max(answer,max(sum))

tt(1,2,a)
tt(2,1,a)

print(answer)