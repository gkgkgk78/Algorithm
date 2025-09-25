



def dfs(visit,graph,now,routes,count):
    if count==len(graph):    
        return routes
    for i in range(len(graph)):
        a1,a2=graph[i]
        if a1==now and visit[i]==0:
            visit[i]=1
            routes.append(a2)
            temp=dfs(visit,graph,a2,routes,count+1)
            if len(temp)!=0:
                return temp
            visit[i]=0
            routes.pop()
    
    return []

def solution(tickets):
    answer = []
    tickets=sorted(tickets,key=lambda x:(x[0],x[1]))
    
    for i in range(len(tickets)):
        a1,a2=tickets[i]
        if a1!='ICN':
            continue
        visit=[0]*len(tickets)
        visit[i]=1
        now=dfs(visit,tickets,a2,[a1,a2],1)
        if len(now)==0:
            continue
        return now
    
