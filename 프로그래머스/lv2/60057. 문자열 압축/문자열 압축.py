def solution(s):
    answer = len(s)
    ans=""
    #문자열을 길이 단위로 해서 나누도록 하자
    for i in range(1, len(s) // 2 + 1):
        last = ""
        temp = []
        j = 0
        t = []
        while (j < len(s)+1):
            t = s[j:j + i]
            if (len(temp) == 0):
                temp.append(t)
            else:
                if (t == temp[-1]):
                    temp.append(t)
                else:
                    if (len(temp) == 1):
                        # temp.append(t[-1])
                        last += temp[-1]
                    else:
                        last = last + str(len(temp)) + temp[-1]
                    temp=[]
                    temp.append(t)
            j=j+i
        if (len(temp)>0):
            last += temp[-1]

        answer=min(answer,len(last))

    return answer