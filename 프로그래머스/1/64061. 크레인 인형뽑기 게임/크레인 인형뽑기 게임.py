from collections import deque

def game(board,now):
    n=len(board)
    m=len(board[0])
    #이제 찾아 내려가도록 하자
    last=0
    for i in range(0,n):
        if board[i][now]!=0:
            last=board[i][now]
            board[i][now]=0
            break
    return last






def solution(board, moves):
    answer = 0
    #터뜨려 사라진 인형의 개수를 구하면 된다
    q=[]
    
    for i in moves:
        a=i
        a-=1
        t=game(board,a)
        
        if t!=0:
            if len(q)==0:
                q.append(t)
            else:
                if q[-1]==t:
                    q.pop()
                    answer+=2
                else:
                    q.append(t)
            
    
    
    
    
    
    
    
    return answer