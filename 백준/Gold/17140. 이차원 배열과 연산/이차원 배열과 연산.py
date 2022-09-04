import sys, copy, heapq
import heapq, math
from itertools import permutations, combinations, product
from collections import deque
from itertools import product
#sys.setrecursionlimit(10 ** 5)
#a=list(product(i,repeat=len(powers)))
#b=list(product(*a)) #리스트 안에 있는 원소들끼리 조합


#input = sys.stdin.readline
#01020306523합격8

from itertools import combinations_with_replacement as cwr
from collections import Counter
time=0
r,c,k=map(int,input().split())
graph=[]
for _ in range(3):
    e=list(map(int,input().split()))
    graph.append(e)
len_row=3
len_col=3

while 1:
    if time >100:
        print(-1)
        break

    if r<=len_row and c<=len_col:
        if  graph[r-1][c-1]==k:
            print(time)
            break

    #r,c연산중 어떤걸 선택할지 정하는 부분
    if len_row>=len_col:
        #r연산 시작 하는 부분
        for i in range(len(graph)):
            e=graph[i]
            te=dict()
            for l in e:
                if l !=0:
                    if l not in te:
                        te[l]=1
                    else:
                        te[l]+=1
            ta=sorted(te.items(),key=lambda te:(te[1],te[0]))
            ui=[]
            for a1,a2 in ta:
                ui.append(a1)
                ui.append(a2)
            graph[i]=ui
            len_col=max(len_col,len(ui))
        #이제 나머지 부분들 채워 주는 부분(0으로)
        for i in range(len(graph)):
            e = graph[i]
            if len(e)!=len_col:
                a1=len_col-len(e)
                aa=[0 for _ in range(a1)]
                graph[i].extend(aa)
            if len(graph[i])>100:
                graph[i]=graph[i][0:100]

        time+=1
    else:#이번에는 c연산을 하려고 함
        #c연산시작하는 부분

        for i in range(0,(len_col)):
            te=dict()
            if i==1:
                efef=32
            for j in range(0,(len_row)):
                if graph[j][i]!=0:
                    if graph[j][i] not in te:
                        te[graph[j][i]]=1
                    else:
                        te[graph[j][i]]+=1
            ta = sorted(te.items(), key=lambda te: (te[1], te[0]))
            ui = []
            for a1, a2 in ta:
                ui.append(a1)
                ui.append(a2)
            a3 = len_row - len(ui)
            if a3<0:
                for _ in range(abs(a3)):
                    graph.append([0 for _  in range(len_col)])
            if a3>0:
                for _ in range(a3):
                    ui.append(0)
            len_row = max(len_row, len(ui))
            ooo=graph
            jh=0

            for _ in range(0,len_row):
                graph[jh][i]=ui[jh]
                jh+=1

        if len_row>100:
            graph=graph[0:100]
        time += 1
