def solution(record):
    answer = []
    #각 uid 별로 Enter, Change 로만 해서 최종 남는것만 확인하면 된다
    total=dict()
    ansL=[]
    rr=[]
    for i in record:
        now=i.split(" ")
        rr.append(now)

    for i in rr:
        now=i[0]
        uid=i[1]
        if now=='Enter' or now=='Change':
            if uid not in total : 
                total[uid]=''
            total[uid]=i[2]
    for i in rr:
        now=i[0]
        uid=i[1]
        if now=='Change':
            continue
        if now=='Enter':
            answer.append(total[uid]+'님이 들어왔습니다.')
        else:
            answer.append(total[uid]+'님이 나갔습니다.')
    
    return answer