def solution(numbers):
    answer = ''
    hi=-1
    total=list(map(str,numbers))
    total=sorted(total,key=lambda x:x*3,reverse=True)
    
    answer="".join(total)
    answer=(int)(answer)
    
    return (str)(answer)