import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n=int(input().rstrip())
for i in range(n):
    t=input().rstrip()
    g=int(input().rstrip())
    f=input().rstrip()

    g1=f[1:-1]


    if len(g1)==0:
        if "D"in t:
            print("error")
        else:
            print("[]")
    else:
        q=deque()
        f= f[1:-1]
        g1=f.split(",")
        for gg in g1:
            q.append(int(gg))
        left=0
        right=0
        ko=0
        exi=0
        for ge in t:
            if ge=="R" and ko%2==0:
                right=1
                left=0
                ko+=1

            elif ge=="R" and ko%2==1:
                right = 0
                left = 1
                ko += 1
            else:
                if len(q)==0:
                    print("error")
                    exi=1
                    break
                if ko==0 or left==1:
                    q.popleft()
                    if len(t)==1 and ge=="D":
                        left=1
                else:
                    q.pop()
        if exi==0:
            if left==1:
                ans=[]
                # for j in range (len(q)):
                #     ans.append(q[j])
                # print(ans)
                print("[",end="")
                for ia in range(len(q)):
                    g2=str(q[ia])
                    if ia ==len(q)-1:
                        print(g2 , end="")
                    else:
                        print(g2+",",end="")
                print("]")
            else:
                q.reverse()
                print("[", end="")
                for ia in range(len(q)):
                    g2 = str(q[ia])
                    if ia == len(q) - 1:
                        print(g2, end="")
                    else:
                        print(g2 + ",", end="")
                print("]")

























