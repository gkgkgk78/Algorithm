import sys
input=sys.stdin.readline
n=int(input().rstrip())
crane=list(map(int,input().split()))
h=int(input().rstrip())
work=list(map(int,input().split()))

crane.sort(reverse=True)
work.sort(reverse=True)

now=0
go=[]
time=0
if work[0]>crane[0]:
    print(-1)
else:
    while 1:
        for i in range(n):
            n1=crane[i]
            if len(work)>0:
                if n1<work[-1]:
                    continue
                for j in work:
                    peek=j
                    if n1>=peek:
                        work.remove(j)
                        h-=1
                        break
            else:
                break
        time+=1
        go.append(h)
        if len(work)==0:
            print(time)
            break