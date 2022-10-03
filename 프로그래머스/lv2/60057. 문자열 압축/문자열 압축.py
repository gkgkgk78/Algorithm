def solution(s):
    answer = int(1e9)
    if len(s)==1:
        return 1
    for i in range(1, len(s) // 2 + 1):
        last = ""
        temp = []
        j = 0
        if i==2:
            j=0
        while j < len(s)+1:
            if len(temp) == 0:
                zz = s[j:j + i]
                temp.append(zz)
            else:
                next_val = s[j:j + i]
                if (temp[-1] == next_val):
                    temp.append(next_val)
                else:

                    if (len(temp) == 1):
                        last = last + temp[0]
                        temp = []
                        temp.append(next_val)
                    else:
                        front_size = len(temp)
                        #if front_size>0:
                        last = last + str(front_size) + temp[-1]
                        # else:
                        #     last=last+temp[0]
                        temp = []
                        temp.append(next_val)
            j = j + i
        if(len(temp)>0):
            last+=temp[-1]

        #print(last,len(last))
            
        answer=min(answer,len(last))
    return answer