def solution(genres, plays):
    answer = []
    
    total_genre=dict()
    total=dict()
    for i in range(len(genres)):
        now_genre=genres[i]
        now_plays=plays[i]
        if now_genre not in total_genre:
            total_genre[now_genre]=plays[i]
            total[now_genre]=[]
        else:
            total_genre[now_genre]+=plays[i]
        total[now_genre].append([plays[i],i])    
    
    #가장 많이 재생된 장르를 수록 하고자 한다
    first=[]
    total_genre=sorted(total_genre.items(),key=lambda x:-x[1])
    for i,_ in total_genre:
        now=total[i]
        now=sorted(now,key=lambda x:(-x[0],x[1]))
        now=now[:2]
        for i1 in now: 
            answer.append(i1[1])
    
    
    return answer