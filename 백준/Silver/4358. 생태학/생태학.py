import sys
input = sys.stdin.readline

total=dict()
count=0
while 1:
    e=input().rstrip()

    if len(e)==0:
        break
    count+=1
    if e not in total:
        total[e]=1
    else:
        total[e]+=1

sort=sorted(total.items(),key=lambda x:x[0])

for l1,l2 in sort:
    e1=round((l2/count)*100,4)
    print(l1,"%.4f"%e1)