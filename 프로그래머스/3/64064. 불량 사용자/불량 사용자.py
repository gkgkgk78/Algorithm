answer=0
total=dict()
visit=dict()
last=dict()
def check(cnt,result,user_id,banned_id):
    global answer
    if cnt==len(banned_id):
        #print(result)
        tt=sorted(result)
        te=""
        #print(result,tt)
        for i in tt:
            te+=i
        if te not in last:
            last[te]=1
            answer+=1
        return
    now=banned_id[cnt]
    temp=total[len(now)]
    
    #이제 탐색을 시작 하면 됨
    for i in temp:
        if visit[i]==0:   
            #이제 확인 작업을 시작 하자
            left=i
            tt=0
            for j in range(len(now)):
                if left[j]!=now[j]:
                    if now[j]=="*":
                        continue
                    else:
                        tt=1
                        break
            if tt==0:
                visit[i]=1
                result.append(i)
                check(cnt+1,result,user_id,banned_id)
                result.pop()
                visit[i]=0
                #break
    
    



def solution(user_id, banned_id):
    global answer,visit
    for i in user_id:
        visit[i]=0
        if len(i)not in total:
            total[len(i)]=[]
        total[len(i)].append(i)
    check(0,[],user_id,banned_id)
    
    
    
    
    
    return answer