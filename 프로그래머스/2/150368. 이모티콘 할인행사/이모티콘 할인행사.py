
answer=[]
service=-1
sales=-1


def solution(users, emoticons):
    global answer
    
    users=sorted(users,key=lambda x:(x[0]))
    visit=[0]*(len(emoticons))
    per=[0]*(len(emoticons))
    dfs(users, emoticons,visit,per,0)
    
    return [service,sales]

def dfs(users, emoticons,visit,per,now):
    if now==len(emoticons):
        cal(users,emoticons,per)
        return
    tt=[10,20,30,40]
    visit[now]=1
    for j in tt:
        per[now]=j
        dfs(users, emoticons,visit,per,now+1)
    visit[now]=0
    
    
def cal(users, emoticons,per):
    global service,sales
    serviceCheck=0
    salesCheck=0
    
    for percen,val in users:
        temp=0
        snow=0
        for i in range(len(emoticons)):
            if percen<=per[i]:
                ss=emoticons[i]*((1-per[i]*0.01))
                temp+=ss
                if temp>=val:
                    serviceCheck+=1
                    snow=1
                    break
        if snow==0:
            salesCheck+=temp
    # print(per,serviceCheck,service)
    if  serviceCheck>=service:  
        if serviceCheck>service:
            service=(serviceCheck)
            sales=(salesCheck) 
        else:
            service=max(service,serviceCheck)
            sales=max(sales,salesCheck)
    
    