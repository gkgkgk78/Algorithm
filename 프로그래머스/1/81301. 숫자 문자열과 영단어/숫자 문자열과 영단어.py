def solution(s):
    answer = ""
    total=dict()
    l1=["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in range(10):
        total[l1[i]]=(str)(i)
    temp=""
    for i in s:
        if "0"<=i<="9":
            answer+=i
        else:
            temp+=i
            
            if temp in total:
                answer+=total[temp]
                temp=""
    
    
    answer=(int)(answer)
    
    
    
    
    return answer