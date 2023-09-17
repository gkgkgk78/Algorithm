#40분
def solution(str1, str2):
    answer = 0
    
    first=[]
    second=[]
    for i in str1:
        first.append(i)
    
    for i in str2:
        second.append(i)

    f_total=dict()
    s_total=dict()
    
    for i in range(len(first)-1):
        if not("a"<=first[i]<="z" or "A"<=first[i]<="Z") :
            continue
        if not("a"<=first[i+1]<="z" or "A"<=first[i+1]<="Z") :
            continue
        nn=first[i]+first[i+1]
        nn=nn.lower()
        if nn not in f_total:
            f_total[nn]=0
        f_total[nn]+=1
    for i in range(len(second)-1):
        if not("a"<=second[i]<="z" or "A"<=second[i]<="Z") :
            continue
        if not("a"<=second[i+1]<="z" or "A"<=second[i+1]<="Z") :
            continue
        nn=second[i]+second[i+1]
        nn=nn.lower()
        if nn not in s_total:
            s_total[nn]=0
        s_total[nn]+=1

    if len(f_total) ==0 and len(s_total)==0:
        answer=65536
    else:
        cross=0
        to=0
        cros=dict()
        #교집합 구하기 
        for a1,a2 in f_total.items():
            if a1 in s_total:
                f1=a2
                f2=s_total[a1]
                cross+=min(f1,f2)
                cros[a1]=1

        #합집합 구하기 
        for a1,a2 in f_total.items():
            if a1 not in s_total:
                to+=a2
        for a1,a2 in s_total.items():
            if a1 not in f_total:
                to+=a2
        for a1,a2 in cros.items():
            f1=f_total[a1]
            f2=s_total[a1]
            to+=max(f1,f2)

        answer=(int)((cross/to)*65536)

    return answer