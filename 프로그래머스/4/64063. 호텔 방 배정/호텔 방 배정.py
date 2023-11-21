import sys
sys.setrecursionlimit(10**5)
answer = []  
total=dict()


def game(now):
    global answer
    if now not in total:
        total[now]=now+1
        answer.append(now)
        return now
    tt=total[now]
    total[now]=game(tt)
    return total[now]
    



def solution(k, room_number):
    
    for i in room_number:
        if i not in total:
            total[i]=i+1
            answer.append(i)
        else:
            game(i)
    
    
    
    
    
    return answer