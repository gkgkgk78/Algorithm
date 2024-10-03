from itertools import combinations

answer=[]
count=0
left_arr=[]
def make(arr,ind,last,rest,sumz,dice):
    if ind==last:
        rest.append(sumz)
        return
    now=dice[arr[ind]]
    for i in range(6):
        make(arr,ind+1,last,rest,sumz+now[i],dice)
    return rest

def fight(now,n,dice):
    global count,answer
    left=list(now)
    right=[]
    for i in range(n):
        if i not in left:
            right.append(i)
    left_arr=make(left,0,n//2,[],0,dice)
    right_arr=make(right,0,n//2,[],0,dice)
    left_arr.sort()
    right_arr.sort()
    now=0
    total=6**(n//2)
    temp=dict()
    temp1=dict()
    for i in left_arr:
        if i not in temp:
            temp[i]=1
        else:
            temp[i]+=1
    for i in right_arr:
        if i not in temp1:
            temp1[i]=1
        else:
            temp1[i]+=1
    for a1,a2 in temp.items():
        check=0
        for i1,i2 in temp1.items():
            if a1>i1:
                check+=a2*i2
            else:
                break
        now+=check
    #print(now,left)
    if now>count:
        count=now
        answer=left
    
    
    

def solution(dice):
    first=[]
    for i in range(len(dice)):
        first.append(i)
    rule=list(combinations(first,len(dice)//2))
    n=len(dice)
    for i in rule:
        fight(i,n,dice)
    for i in range(len(answer)):
        answer[i]+=1
    answer.sort()
      
    return answer