def solution(s):
    answer = []
    #순서있는 열거 또는 순서를 따르는 요소들의 모음을 튜플이라고 한다
    total=[]
    temp=[]
    la=['{', '}', ',' ]
    check=dict()
    tt=""
    s=s[1:-1]
    ss=list(map(str,s.split("}")))
    #print(ss)
#     for i in s:
        
#         if i =='}':
            
#             if len(temp)!=0:
#                 total.append(temp)
#             temp=[]
#         else:
#             if i not in la:
#                 tt+=i
#             else:
#                 print(tt)
#                 #temp.append((int)(tt))
#                 tt=""

    for i in ss:
        i=i.replace(",{","")
        i=i.replace("{","")
        temp=[]
        tt=""
        for j in i:
            if j!=",":
                tt+=j
            else:
                temp.append(int(tt))
                tt=""
        #print(i)
        if len(tt)>0:
            temp.append(int(tt))
        total.append(temp)
    #total.append(temp)
    
    total=sorted(total,key=lambda x: len(x))
    #print(total)
    for i in total:
        for j in i:
            if j not in check:
                check[j]=1
                answer.append(j)
    
    
    
    
    
    return answer