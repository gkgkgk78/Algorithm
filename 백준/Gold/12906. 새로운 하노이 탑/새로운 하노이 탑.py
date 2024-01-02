import sys
from collections import deque

input = sys.stdin.readline

first=""
second=""
third=""

visit=dict()

for i in range(3):

    tt=list(map(str,input().split()))
    if (int)(tt[0])>0:
        a2=tt[1]
        temp=list(map(str,a2.rstrip()))
        if i==0:
            first=a2
        elif i==1:
            second=a2
        else:
            third=a2


def make(a1,a2,a3):
    la=""
    la+="0"
    la+=a1
    la+="1"
    la+=a2
    la+="2"
    la+=a3
    return la

tt=make(first,second,third)
visit[tt]=1


def check(li,ch):
    for i in li:
        if i!=ch:
            return 0
    return 1


def bfs(index,a1,a2,a3):
    q=deque()
    tt=make(a1,a2,a3)
    visit[tt]=1
    q.append((index,a1,a2,a3))
    while q:
        now,temp1,temp2,temp3=q.popleft()
        l1=check(temp1,"A")
        l2=check(temp2,"B")
        l3=check(temp3,"C")

        if l1+l2+l3==3:
            return now
        #이제 넣어 줘야 한다
        if len(temp1)>0:
            last=temp1[-1]
            s1=make(temp1[:-1],temp2+last,temp3)
            if s1 not in visit:
                visit[s1]=1
                q.append((now+1,temp1[:-1],temp2+last,temp3))
            s1 = make(temp1[:-1], temp2, temp3+last)
            if s1 not in visit:
                visit[s1] = 1
                q.append((now + 1, temp1[:-1], temp2, temp3+last))
        if len(temp2)>0:
            last=temp2[-1]
            s1=make(temp1+last,temp2[:-1],temp3)
            if s1 not in visit:
                visit[s1]=1
                q.append((now+1,temp1+last,temp2[:-1],temp3))
            s1 = make(temp1,temp2[:-1],temp3+last)
            if s1 not in visit:
                visit[s1] = 1
                q.append((now + 1, temp1,temp2[:-1],temp3+last))
        if len(temp3)>0:
            last=temp3[-1]
            s1=make(temp1+last,temp2,temp3[:-1])
            if s1 not in visit:
                visit[s1]=1
                q.append((now+1,temp1+last,temp2,temp3[:-1]))
            s1 = make(temp1,temp2+last,temp3[:-1])
            if s1 not in visit:
                visit[s1] = 1
                q.append((now + 1, temp1,temp2+last,temp3[:-1]))

print(bfs(0,first,second,third))