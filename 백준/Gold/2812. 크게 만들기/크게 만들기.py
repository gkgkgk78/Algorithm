import sys

input = sys.stdin.readline

n,k=map(int,input().split())
e=list(map(int,input().rstrip()))

q=[]
ind=0

for i in e:
    if len(q)==0:
        q.append(i)
    else:
        if ind==k:
            q.append(i)
        else:
            if q[-1]<i:
                while q:
                    if q[-1]<i:
                        q.pop()
                    else:
                        break
                    ind+=1
                    if ind==k:
                        break
                q.append(i)
            else:
                q.append(i)
if ind !=k:
    q=q[:-(k-ind)]
print(''.join(map(str, q)))