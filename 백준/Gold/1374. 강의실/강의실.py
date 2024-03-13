import heapq
import sys
input = sys.stdin.readline

n=int(input().rstrip())
e=[]
for _ in range(n):
    a1,a2,a3=map(int,input().split())
    e.append((a1,a2,a3))
e=sorted(e,key=lambda x:(x[1],x[2]))

q=[]
count=1
heapq.heappush(q,e[0][2])
for i in range(1,n):
    _,a1,a2=e[i]
    head=heapq.heappop(q)
    if head<=a1:
        heapq.heappush(q,a2)
    else:
        heapq.heappush(q,head)
        count+=1
        heapq.heappush(q,a2)
print(count)