from collections import deque
answer=0
def game(q1,q2,to):
    global answer
    #q1이 총합이 더 큰 리스트 임
    left=0
    right=0
    now=q1[0]
    while right<len(q1):
        right+=1
        if right==len(q1):
            break
        now += q1[right]
        if now>to:
            while 1:
                now-=q1[left]
                left+=1
                if left ==right:
                    break
                if now<=to:
                    break
    #이제 다른곳으로 넘기면 된다
    while left>0:
        q2.append(q1.popleft())
        left-=1
        answer+=1
    
    
                

def solution(queue1, queue2):
    global answer
    #각 큐의 원소 합이 같도록 만들려고 한다
    #필요한 작업의 최소 횟수를 구하도록 하자
    to=sum(queue1)+sum(queue2)
    to=to//2
    toa=len(queue1)+len(queue2)
    for i in queue1:
        if i>to:
            return -1
    for i in queue2:
        if i>to:
            return -1
    #그렇지 않으면 이제 파악을 해보도록 하자
    ch=0
    queue1=deque(queue1)
    queue2=deque(queue2)
    s1=sum(queue1)
    s2=sum(queue2)
    while 1:
        if s1== s2:
            return answer
        if s1>s2:
            aa=queue1.popleft()
            s1-=aa
            s2+=aa
            queue2.append(aa)
        else:
            aa=queue2.popleft()
            s2-=aa
            s1+=aa
            queue1.append(aa)
        ch+=1
        answer+=1
        if ch>300000:
            return-1
    
    
    
    return answer




