def solution(phone_book):
    answer = True
    total=dict()
    for i in phone_book:
        total[i]=1
    
    
    for i in phone_book:
        temp=""
        for j in (i):
            temp+=j
            if temp in total and temp!=i:
                return False
    
    return True