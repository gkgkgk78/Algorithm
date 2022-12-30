import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline
n=int(input().rstrip())
ans=-sys.maxsize
tree=[[]for _ in range(n+1)]

for _ in range(n-1):
    a1,a2,a3=map(int,input().split())
    tree[a1].append((a2,a3))

answer=0
def dfs(vertex,value):
    global answer
    if len(tree[vertex])==0:
        return value

    left=0
    right=0
    jason=[]
    for i in range(len(tree[vertex])):
        down_left=tree[vertex][i]
        left=dfs(down_left[0],down_left[1]+value)
        jason.append(left)

    if len(tree[vertex])>=2:
        jason.sort()
        answer=max(answer,jason[-1]+jason[-2]-value*2)
    else:
        answer = max(answer, jason[0] - value )
    return(max(jason))

ans=dfs(1,0)
print(answer)