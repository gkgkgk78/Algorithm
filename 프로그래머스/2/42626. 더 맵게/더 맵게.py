import heapq
def solution(scoville, K):
    answer = 0
    q=[]
    cnt=0
    for i in scoville:
        heapq.heappush(q,(i))
    while q:
        if len(q)<=1:
            break
        a1=heapq.heappop(q)
        a2=heapq.heappop(q)
        if a1>=K:
            return cnt
        heapq.heappush(q,(a1+a2*2))
        cnt+=1
    a1=heapq.heappop(q)
        
    if a1>=K:
        return cnt
    
    
    return -1