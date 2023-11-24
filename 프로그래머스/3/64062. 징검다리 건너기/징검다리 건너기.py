def test(stones,mid,k):
    an=0
    for i in stones:
        if mid>i:
            an+=1
        else:
            an=0
        if an>=k:
            return -1
        
    return 1

def solution(stones, k):
    answer = 0
    left=-1
    #right=max(stones)+1
    right=200000000
    while left+1<right:
        mid=(left+right)//2
        tt=test(stones,mid,k)
        if tt==1:
            left=mid
        else:
            right=mid
        #print(tt,left,right)
    answer=left
    
    
    return answer