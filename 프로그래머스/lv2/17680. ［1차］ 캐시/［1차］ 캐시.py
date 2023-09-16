def solution(cacheSize, cities):
    answer = 0
    
    #캐시 크기에 따른 실행 시간 측정 프로그램을 작성 해보도록 하자
    total=dict()
    test=0
    time=0
    for i in cities:
        i=i.lower()
        if cacheSize==0:
            answer+=5
            continue
        if i not in total:
            answer+=5
            if test<cacheSize:
                total[i]=time
                test+=1
            elif test==cacheSize:
                n1=""
                n2=10**5
                #이제 가장 처음에 사용한거 고르면 된다
                for a1,a2 in total.items():
                    if a2<n2:
                        n2=a2
                        n1=a1
                del total[n1]
                total[i]=time
        else:
             total[i]=time
             answer+=1   
        
        time+=1
        
        
    
    
    return answer