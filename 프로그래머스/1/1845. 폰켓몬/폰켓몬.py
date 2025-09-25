def solution(nums):
    answer = 0    
    #n/2마리를 선택하려고 하는데, 폰켓몬을 어떻게 고를 것이냐??
    temp=set(nums)
    if len(temp)>=len(nums)//2:
        return len(nums)//2
    else:
        return len(temp)
    
    
    return answer