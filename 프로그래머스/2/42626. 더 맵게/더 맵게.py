import heapq
def solution(scoville, K):
    answer = 0
    #매운것을 좋아하는 leo는 모든 음식의 스코빌 지수를 k이상으로 만들고 싶어 한다
    #섞어야 하는 최소 횟수를 return 하도록 하라
    q=[]
    check=0
    for i in scoville:
        heapq.heappush(q,i)
    while q:
        a1=heapq.heappop(q)
        if a1>=K:
            check=1
            break
        if len(q)==0:
            break
        a2=heapq.heappop(q)

        heapq.heappush(q,a1+a2*2)
        answer+=1
    if check==1:
        return answer
      
    
    return -1