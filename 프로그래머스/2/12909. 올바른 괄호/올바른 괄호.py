from collections import deque

def solution(s):
    answer = True
    q=deque()
    for i in s : 
        if i=='(':
            q.append('(')
        else:
            if len(q)==0:
                return False
            else:
                q.popleft()
    if len(q)>0:
        return False
    return answer