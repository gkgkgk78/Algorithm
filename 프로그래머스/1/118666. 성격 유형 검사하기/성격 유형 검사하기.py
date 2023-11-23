def solution(survey, choices):
    answer = ''
    #성격 유형 검사지 만들자!
    total=[["R","T"],["C","F"],["J","M"],["A","N"]]
    check=dict()
    ha=[3,2,1,0,1,2,3]
    for i in total:
        check[i[0]]=0
        check[i[1]]=0
    
    
    for i in range(len(survey)):
        aa=survey[i]
        a1=aa[0]
        a2=aa[1]

        #이제 점수 파악을 해보도록 하자
        nex=choices[i]-1
        if nex<=2:
            check[a1]+=ha[nex]
        elif nex>=4:
            check[a2]+=ha[nex]
    for i in total:
        a1=i[0]
        a2=i[1]
        if check[a1]>=check[a2]:
            answer+=a1
        else:
            answer+=a2
    
    
    
    
    
    
    
    return answer