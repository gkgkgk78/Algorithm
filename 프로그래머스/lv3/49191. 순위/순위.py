from collections import Counter

def solution(n, results):
    answer = 0
    graph=[[0]*(n) for _ in range(n)]
    
    for a1,a2 in results:
        a1-=1
        a2-=1
        graph[a1][a2]=1
        graph[a2][a1]=-1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k]==1 and graph[k][j]==1:
                    graph[i][j]=1
                    graph[j][i]=-1
    for i in range(n):
        temp=Counter(graph[i])
        if temp[0]==1:
            answer+=1
    
    
    return answer