def solution(stones, k):
    answer = 0
    
    left=0
    right=200000001

    
    while left+1<right:
        mid=(left+right)//2
        aa=go(stones,k,mid)
        if aa==1:
            right=mid  
        else:
            left=mid
    answer=left+1
    
    
    return answer


def go(stone,k,users):
    
    count=0
    cc=0
    for i in stone:
        if i <= users:
            cc+=1
            if cc>=k:
                return 1
        else:
            cc=0

    return 0
   
    
    
    
    
    
    