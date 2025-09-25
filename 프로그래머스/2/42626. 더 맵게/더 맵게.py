import heapq
def solution(scoville, K):
    answer = 0
    q=[]
    for i in scoville:
        heapq.heappush(q,i)
    temp=0
    while q:
        now=heapq.heappop(q)
        if now>=K:
            return temp
        if len(q)==0:
            break
        now1=heapq.heappop(q)
        heapq.heappush(q,now+now1*2)
        temp+=1
    return -1
    