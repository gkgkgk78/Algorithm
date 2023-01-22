import sys
input = sys.stdin.readline
graph=[[0]*100 for _ in range(100)]
n=int(input().rstrip())
for _ in range(n):
    a1,a2=map(int,input().split())
    a1-=1
    a2-=1
    if a1==14:
        a1=14
    for i in range(a1,a1+10):
        for j in range(a2,a2+10):
            graph[i][j]+=1

answer=-sys.maxsize

def check(x,y,width,height):
    #가로축 확인
    temp=0
    for i in range(x,x+width+1):
        for j in range(y,y+height+1):
            if graph[i][j]==0:
                return -1
            temp+=1
    return temp



def go(x,y):
    now=-sys.maxsize
    for i in range(0,100):
        if x+i>=100:
            break
        for j in range(0,100):
           if j + y >= 100:
               break
           temp=check(x,y,i,j)
           if (temp)>=0:
               now=max(now,temp)

    return now


for i in range(100):
    for j in range(100):
        if graph[i][j]==0:
            continue
        temp=go(i,j)
        answer=max(temp,answer)


print(answer)
