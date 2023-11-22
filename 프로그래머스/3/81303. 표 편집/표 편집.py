def solution(n, k, cmd):
    answer = ''
    # 표의 행을 선택,삭제,복구하는 프로그램 작성하자
    total = dict()
    delete = []
    for i in range(n):
        total[i] = [i - 1, i + 1, "O"]  # 현재 인덱스 현재 상태를 의미를 한다
    total[0] = [n - 1, 1, "O"]
    total[n - 1] = [n - 2, 0, "O"]
    now = k  # 이것은 행을 의미하는 거임
    for i in cmd:
        
        e = list(map(str, i.split(" ")))
        if e[0] == "U":
            # 이제 거슬러 올라가면서 가보도록 하자
            cnt = (int)(e[1])
            while cnt > 0:
                before, nex, no = total[now]
                now = before
                cnt -= 1
        elif e[0] == "D":
            cnt = (int)(e[1])
            while cnt > 0:
                before, nex, no = total[now]
                now = nex
                cnt -= 1
        elif e[0] == "C":
            # 현재 행 삭제한후 바로 아래행을 선택 하도록 한다
            before, nex, no = total[now]
            total[now] = [before, nex, "X"]  # 현재 행 삭제 하도록 하고
            # 그전께 내 다음 가리키게
            before1, nex1, no1 = total[before]
            total[before] = [before1, nex, no1]
            # 그다음께 내전꺼 가리키게 해야 한다
            before1, nex1, no1 = total[nex]
            total[nex] = [before, nex1, no1]
            delete.append(now)
            now1=now
            now = nex
            if nex ==0:
                now=before
            
        else:
            temp = delete[-1]
            delete.pop()
            before, nex, no = total[temp]
            before1, nex1, no1 = total[nex]
            total[nex] = [temp, nex1, no1]

            total[temp] = [before1, nex, "O"]  # 현재 행 삭제 하도록 하고
            # 그전께 내 다음 가리키게
            before2, nex2, no2 = total[before1]
            total[before1] = [before2, temp, no2]
            # 그다음께 내전꺼 가리키게 해야 한다
        #print(now)
    for i in range(n):
        aa, aaa, xx = total[i]
        answer += xx

    return answer