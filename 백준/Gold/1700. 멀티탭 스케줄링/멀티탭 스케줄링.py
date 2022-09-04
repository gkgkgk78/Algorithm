import sys, copy, heapq
import heapq, math
from itertools import permutations, combinations, product
from collections import deque
from itertools import product
#sys.setrecursionlimit(10 ** 5)
#a=list(product(i,repeat=len(powers)))
#b=list(product(*a)) #리스트 안에 있는 원소들끼리 조합




from itertools import combinations_with_replacement as cwr
from collections import Counter
input = sys.stdin.readline


n,m=map(int,input().split())

#check=[0 for _ in range(m+1)]#남아있는 실행 횟수를 담은 리스트
check=dict()

now=list(map(int,input().split()))#실행 순서를 담은 리스트
now.insert(0,0)

for i in range(1,m+1):
    if now[i] not in check:
        check[now[i]]=1
    else:
        check[now[i]] +=1


plug=[0 for _ in range(n+1)]#멀티탭을 의미함
jo=1
t=0
for i in range(1,m+1):
    if(now[i] not in plug):
        plug[jo]=now[i]
        check[now[i]]-=1
        jo+=1
    else:
        check[now[i]] -= 1
    t=i
    if(jo==n+1):
        break


coun=0
for i in range(t+1, m+1):
    if now[i] in plug:
        check[now[i]]-=1#실행 횟수를 감소하고
        continue
    else:#이제 새로 플러그에 꽂혀야함
        s=0
        for k in range(1,n+1):
            if(plug[k]==0):#플러그에 빈공간이 존재 했네?
                plug[k]=now[i]
                check[now[i]] -= 1  # 실행 횟수를 감소하고
                s=1
                break
             #존재 하지 않았음 , 그럼 이제 무엇을 빼낼것인가?
                #멀티 탭에 남은 것중에서 남은 횟수가 더 적은 것을 빼내야 하겠지
                #현재 플러그에서 가장 적게 남은 횟수를 파악해보자
        #만약 현재 플러그에서 남은실행 횟수가 0이라면 그것을 제거해 주자
        if s==1:
            continue
        for k in range(1,n+1):
            if(check[plug[k]]==0):
                plug[k]=now[i]
                check[now[i]]-=1
                coun += 1
                s=1
                #print(plug)

                break
        if s==1:
            continue

        min_co=999#남은 횟수 파악
        min_ww=-1#꽂을 인덱스

        for l in range(1,n+1):
            #plug를 돌면서 가장 뒤에 있는거를 확인해 보고자 함
            op=45
            for kk in range(i+1,m+1):
                if(plug[l]==now[kk]):
                    min_ww=max(min_ww,kk)
                    break
        min_co=now[min_ww]
        #이렇게 해서 찾았는데 찾은 인덱스에 해당되는 check보다 같거나 
        #큰게 존재를 한다면 변경을 해줘야 겠다
        plug[plug.index(min_co)]=now[i]
        check[now[i]] -= 1
        coun+=1
        #print(plug)
print(coun)

