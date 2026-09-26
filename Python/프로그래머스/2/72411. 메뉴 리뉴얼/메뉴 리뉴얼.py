from itertools import combinations
def solution(orders, course):
    answer = []
    
    for i in course:
        now=i
        total=dict()
        ma=-1
        #가장 많이 함께 주문된 단품 메뉴 조합을 따르면 된다
        for j in orders:
            if len(j)<now:
                continue
            le=list(combinations(j,now))
            for k in range(len(le)):
                temp=""
                nn=le[k]
                for l in nn:
                    temp+=l
                le[k]=''.join(sorted(temp))
            for k in le:
                if k not in total:
                    total[k]=0
                total[k]+=1
                ma=max(ma,total[k])
        if ma>=2:
            for a1,a2 in total.items():
                   if a2==ma:
                        answer.append(a1)
        answer.sort()
    
    return answer