
def check(rocks,mid):
    
    be=0
    count=0
    for i in rocks:
        now=i-be
        if now>=mid:
            be=i
        else:
            count+=1
    return count
    


def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    
    left=0
    right=distance+1
    while left+1<right:
        mid=(left+right)//2
        now=check(rocks,mid)
        if now<=n:
            left=mid
        else:
            right=mid
    
    
    return left