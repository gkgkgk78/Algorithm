import heapq

def solution(files):
    answer = []
    
    q=[]
    eee=0
    for aa in files:
        head=""
        number=""
        tail=""
        index=0
        for i in range(len(aa)):
            if "0"<=aa[i]<="9":
                
                break
            else:
                head+=aa[i].lower()
            index+=1
        cc=index
        for i in range(index,index+5):
            if i>=len(aa):
                break
            if "0"<=aa[i]<="9":
                number+=aa[i]
            else:
                break
            cc+=1
        number=(int)(number)
        # if cc<len(aa):
        #     tail="".join(aa[cc:])
        heapq.heappush(q,(head,number,eee,aa))
        eee+=1
    
    while q:
        a1,a2,a3,a4=heapq.heappop(q)
        print(a1,a2,a3,a4)
        answer.append(a4)
            
    
    
    
    
    return answer