def solution(str1, str2):
    answer = 0
    
    str1=str1.lower()
    str2=str2.lower()
    #1.각 문자별로 두글자씩 끊어서 만듬 + dict 도 같이
    
    firstTotal=[]
    firstDi=dict()
    
    for i in range(len(str1)):
        first=""
        second=""
        if i+1>=len(str1):
            break
        first=str1[i]
        second=str1[i+1]
        if first.isalpha()==False or second.isalpha()==False:
            continue

        ne=first+second
        if ne not in firstDi:
            firstDi[ne]=1
        else:
            firstDi[ne]+=1
        firstTotal.append(ne)
        
    secondTotal=[]
    secondDi=dict()    
    for i in range(len(str2)):
        first=""
        second=""
        if i+1>=len(str2):
            break
        first=str2[i]
        second=str2[i+1]
        if first.isalpha()==False or second.isalpha()==False:
            continue
        ne=first+second
        if ne not in secondDi:
            secondDi[ne]=1
        else:
            secondDi[ne]+=1
        secondTotal.append(ne)        
    
    if len(firstTotal)==0 and len(secondTotal)==0:
        return 65536
    
    #2.교집합 => dict1 돌면서 dict2 에 있으면 min으로 해야함
    go=0
    for i1,i2 in firstDi.items():
        if i1 in secondDi:
            first=i2
            second=secondDi[i1]
            go+=min(first,second)
    
    #3 두개 합쳐서 set으로 만듦 그후에, 교집합에 있는거로 개수 수정해 줘야함
    ui=0
    to=firstTotal+secondTotal
    to=set(to)
    for i1,i2 in firstDi.items():
        if i1 in secondDi:
            first=i2
            second=secondDi[i1]
            ne=max(first,second) 
            if ne!=1:
                ui+=(ne-1)
    for i1,i2 in firstDi.items():
        if i1 not in secondDi:
            ui+=i2-1
    for i1,i2 in secondDi.items():
        if i1 not in firstDi:
            ui+=i2-1
    ui+=len(to)
    
    
    return (int)((go/ui)*65536)