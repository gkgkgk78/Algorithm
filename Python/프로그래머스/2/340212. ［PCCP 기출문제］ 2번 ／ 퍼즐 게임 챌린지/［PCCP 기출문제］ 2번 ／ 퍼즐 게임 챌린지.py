
def check(diffs,times,limit,mid):
    temp=0
    for i in range(len(diffs)):
        di=diffs[i]
        ti=times[i]
        if di<=mid:
            temp+=ti
        else:
            be=times[i-1]
            temp=temp+((di-mid)*(ti+be)+ti)
        if temp>limit:
            return 0
    return 1


def solution(diffs, times, limit):
    answer = 0
    left=0
    right=max(diffs)+1

    while left+1<right:
        mid=(left+right)//2
        now=check(diffs,times,limit,mid)
        if now==1:
            right=mid
        else:
            left=mid
    answer=right
    
    return answer