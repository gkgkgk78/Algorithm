def solution(targets):
    answer = 1
    #모든 폭격 미사일을 요격하기 위해 필요한 요격 미사일 수의 최솟값 return 
    targets=sorted(targets,key=lambda x:(x[1]))
    end=targets[0][1]
    for s,e in targets:
        if s<end:
            continue
        else:
            answer+=1
            end=e
    
    return answer