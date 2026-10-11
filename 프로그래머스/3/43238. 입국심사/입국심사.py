def solution(n, times):
    answer = 0
    left= 0
    right=max(times)*n+1
    
    while left+1<right:
        mid=(left+right)//2
        ch=check(times,mid)
        # print(left,right,mid,ch)
        if ch>=n:
            right=mid
        else:
            left=mid
    answer=right
    
    return answer


def check(times,mid):
    temp=0
    for i in times:
        temp+=(mid//i)
    return temp