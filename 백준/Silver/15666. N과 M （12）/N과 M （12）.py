import sys, copy
import heapq,math
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())

gl=list(map(int,input().split()))
gl.sort()
st=[]

visit=[0]*(10001)
def dfs(depth,idx,a,b):
    global ho1
    if depth==b:
        ae=tuple(st)
        ho1.append(ae)
        return
    for i in range(a):

            if len(st)==0:
                st.append(gl[i])
                dfs(depth+1,i,a,b)
                st.pop()
            else:
                if st[-1]<=gl[i]:
                    st.append(gl[i])
                    dfs(depth + 1, i, a, b)
                    st.pop()

ho1=[]
dfs(0,0,n,m)

ho1=list(set(ho1))
ho1.sort()

for i in range(len(ho1)):
    print(*ho1[i])