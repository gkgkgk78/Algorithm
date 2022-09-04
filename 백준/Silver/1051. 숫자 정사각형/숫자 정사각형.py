import sys,copy
from itertools import combinations

from collections import deque

input=sys.stdin.readline



a,b=map(int,input().split())
graph=[]
min=-4
graph=[list(map(int,input().rstrip())) for _ in range(a)]



for i in range(a):
    for j in range(b):
        for k in range(j+1,b):
            if graph[i][j]==graph[i][k]:
                t=k-j
                #i+t j , i+t k
                if i+t<a:
                    if graph[i+t][j]== graph[i+t][k] :
                        if graph[i+t][j]== graph[i][j] and graph[i+t][k]==graph[i][k]:
                            if (t+1)*(t+1)>min:
                                min=(t+1)*(t+1)

if min==-4:
    print(1)
else:
    print(min)


































