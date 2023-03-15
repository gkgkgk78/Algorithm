



def search(number) :
    length = len(number)
    if length == 1 or '1' not in number or '0' not in number:
        return True
    
    mid = length // 2
    if number[mid] == '0':
        return False
    
    return search(number[:mid]) and search(number[mid+1:])


def solution(numbers):
    answer = []
    perfect = [ 2**x - 1 for x in range(50)]
    
    for l in numbers:
        now=bin(l)[2:]
        now_len=len(now)
        for k in perfect:
            if now_len<=k:
                now='0'*(k-now_len)+now
                break
            
        next=search(now)
        if next==1:
            answer.append(1)
        else:
            answer.append(0)
    
    
    
    
    
    return answer