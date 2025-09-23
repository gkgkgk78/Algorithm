answer=0
def dfs(numbers,target,calculates,index):
    global answer
    if index==len(numbers):
        temp=0
        for i in range(len(calculates)):
            if calculates[i]=='-':
                temp-=numbers[i]
            else:
                temp+=numbers[i]  
        if temp==target:
            answer+=1
        return
    calculates[index]='-'
    dfs(numbers,target,calculates,index+1)
    calculates[index]='+'
    dfs(numbers,target,calculates,index+1)
    
    

def solution(numbers, target):
    global answer
    cal=[0]*(len(numbers))
    dfs(numbers,target,cal,0)
    return answer
    