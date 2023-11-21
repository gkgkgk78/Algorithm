def solution(gems):
    answer = []
    #쇼핑을 하러 가자
    #특정 범위의 물건들을 싹쓰링 하는 습관이 있다
    #진열된 모든 종류의 보석을 적어도 1개 이상 포함하는가장 짧은 구간을 찾아서 구매 하자?
    
    now=set(gems)
    total=dict()
    for i in now:
        total[i]=0
    last=[]
    check=len(now)
    #슬라이딩 윈도우로 해서 파악 해보도록 하자
    find=1
    left=0
    right=0
    total[gems[0]]=1
    if find==check:
        last.append((right-left+1,left,right))
    while right<len(gems):
        
        right+=1
        if right==len(gems):
            break
        if total[gems[right]]==0:
            find+=1
        total[gems[right]]+=1
        #print(left,right,find,check)
        if find>=check:
            if find>=check:
                last.append((right-left+1,left,right))
            #이제 왼쪽에서 부터 댕겨 오면서 해야 함
            while 1:
                if left==right:
                    break
                total[gems[left]]-=1
                if total[gems[left]]==0:
                    find-=1
                left+=1
                if find<check:
                    break
                else:
                    last.append((right-left+1,left,right))
    
    last=sorted(last,key=lambda x:(x[0],x[1]))
    #print(last[0][1])
    answer.append(last[0][1]+1)
    answer.append(last[0][2]+1)
    
    
    
    
    return answer