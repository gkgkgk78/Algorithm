import sys
import math

input=sys.stdin.readline

n = int(input())


while n>0:
    a1,a2=map(int,input().split())
    t=list(map(int,input().split()))
    check=a2
    count=0
    while 1:
        if t[0] != max(t):
              t.append(t[0])
              if check!=0:
                  check=check-1
                  del (t[0])

              elif check==0:
                  del (t[0])
                  check=len(t)-1


        elif t[0]==max(t):
            if check==0:
                print(count+1)
                break
            else:
                check=check-1
                count=count+1
                del (t[0])








    n=n-1