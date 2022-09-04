import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


a,b=map(int,input().split())

t=list(map(int,input().split()))



count=0
inte=0
start=0
end=0
g=[]
for start in range(a):

    while inte<b and end<a :
        inte=t[end]+inte
        end+=1

    if inte>=b:
       count=count+1
       t23=end-start
       g.append(t23)
    inte=inte-t[start]

if count==0:
    print(count)
else:
    print(min(g))

# print(count,g)
# print(min(g))