import sys
def game(stones,k,mid):
    

    temp=0
    for i in range(len(stones)):
        if stones[i]<mid:
            temp+=1
            
            if temp>=k:
                return -1
        else:
            temp=0
    
    return 1


def finds(stones,k):

    
    left=0
    right=max(stones)+1
    mama=-1
    while left+1<right:
        mid=(left+right)//2
        aa=game(stones,k,mid)
        #print(left,right)
        if aa==1:
            left=mid
            mama=max(mama,left)
        else:
            right=mid
    return mama
            
    
    

def solution(stones, k):
    answer = 0
    
    answer=finds(stones,k)
    
    
    return answer