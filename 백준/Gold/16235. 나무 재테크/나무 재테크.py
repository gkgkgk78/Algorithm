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

#봄에는 자신나이만큼 양분을 먹고 나이가 1증가함
#여러개의 나무가 있다면 나이가 어린 나무부터 양분을 먹는다.
#양분이 부족하면 죽는다.
#여름에는 봄에 죽은 나무가 양분으로 변하게 된다.
#죽은 나무마다 나이를 2로 나눈값이 나무가 있던 칸에 양분으로 추가 된다
#가을에는 나무가 번식한다.인접한 8개 칸에 나이가 1인 나무가 생긴다
#땅을 돌아다니면서 땅에 양분을 추가한다.



n,m,ka=map(int,input().split())
tree=[[deque() for _ in range(n+1)] for _ in range(n+1)]

food=[[5 for _ in range(n+1)] for _ in range(n+1)]
got=[]
for l in range(n):
    e=list(map(int,input().split()))
    for j in range(len(e)):
        got.append((l+1,j+1,e[j]))


for l in range(m):
    a1,a2,a3=map(int,input().split())
    tree[a1][a2].appendleft(a3)


year=0
let=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
while 1:

   for i in range(1,n+1):
       for j in range(1,n+1):
           if(len(tree[i][j])>=1):
               for k in range(len(tree[i][j])):
                   if food[i][j]-tree[i][j][k]>=0:
                       food[i][j] -=tree[i][j][k]
                       tree[i][j][k]+=1
                   else:
                       for _ in range(k,len(tree[i][j])):
                           food[i][j] +=tree[i][j].pop()//2
                       break

    #이제 가을 차례
   for i in range(1, n + 1):
       for j in range(1, n + 1):
           for k in tree[i][j]:
                if k%5==0:
                    #이때는 번식이 가능함
                    for w1,w2 in let:
                        f1=w1+i
                        f2=w2+j
                        if 1<=f1<=n and 1<=f2<=n:
                            tree[f1][f2].appendleft(1)

    #겨울
   for w1,w2,w3 in got:
        food[w1][w2]+=w3
   year+=1

   if year==ka:
        su=0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                su+=len(tree[i][j])
        print(su)
        break