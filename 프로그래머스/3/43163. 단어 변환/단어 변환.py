import sys
answer=sys.maxsize
def check(before,after):
    count=0
    for i in range(len(before)):
        if before[i]!=after[i]:
            count+=1
    if count==1:
        return 1
    return 0
    
def dfs(now,target,words,visit,count):
    global answer
    if now==target:
        answer=min(answer,count)
        return
        
    for i in range(len(words)):
        if visit[i]==1:
            continue
        if check(now,words[i])==1:
            visit[i]=1
            dfs(words[i],target,words,visit,count+1)
            visit[i]=0

def solution(begin, target, words):
    global answer
    #target이 words안에 없을시에 0 리턴
    
    if target not in words:
        return 0
    
    dfs(begin,target,words,[0]*len(words),0)
    
    
    return answer