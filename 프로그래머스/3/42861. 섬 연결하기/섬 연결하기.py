import heapq

parents=[]

def find(i):
    if parents[i]==i:
        return i
    parents[i]=find(parents[i])
    return parents[i]

def union(a1,a2):
    z1=find(a1)
    z2=find(a2)
    if z1<z2:
        parents[z2]=a1
    else:
        parents[z1]=z2

def make():
    for i in range(1,len(parents)):
        parents[i]=i
    
    


def solution(n, costs):
    global parents
    answer = 0
    parents=[0]*(n+1)    
    make()
    co=sorted(costs,key=lambda x:(x[2]))
    
    for v1,v2,value in co:
        f1=find(v1)
        f2=find(v2)
        if f1!=f2:
            union(f1,f2)
            answer+=value
    
    return answer