import sys
input = sys.stdin.readline
n = int(input().rstrip())
# 전체 그래프 형태의 모양을 입력 받고자 함
graph = [[0 for _ in range(n)] for _ in range(n)]
favorite = []  # 여기서 전체 순서를 결정해서 진행 하도록 하고자 함

# 전체 입출력을 받아 주는 부분
for _ in range(n * n):
    ee = list(map(int, input().split()))
    favorite.append(ee)


def check_favorite(check, favorite_student):
    check_max = -sys.maxsize
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    find = []

    for i in range(n):
        for j in range(n):
            # 칸이 비어 있으면서
            if (graph[i][j] == 0):
                check_student = 0
                for k in range(4):
                    zx = i + dx[k]
                    zy = j + dy[k]
                    if (0 <= zx < n and 0 <= zy < n):
                        # 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다
                        if (graph[zx][zy] in favorite_student):
                            check_student += 1
                if (check_student > check_max):
                    find = []
                    find.append((i, j))
                    check_max=check_student
                elif (check_student == check_max):
                    find.append((i, j))


    return find


def check_empty(check):
    check_max = -sys.maxsize
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    find = []
    for i, j in check:
        # 칸이 비어 있으면서
        if (graph[i][j] == 0):
            check_student = 0
            for k in range(4):
                zx = i + dx[k]
                zy = j + dy[k]
                if (0 <= zx < n and 0 <= zy < n):
                    # 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다
                    if (graph[zx][zy] == 0):
                        check_student += 1
            if (check_student > check_max):
                find = []
                find.append((i, j))
                check_max=check_student
            elif (check_student == check_max):
                find.append((i, j))

    return find

def last_cal(total,favorite):

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    find = 0
    ind=0
    for key,val in total.items():
            i,j=val
            favo=favorite[ind]
            fav=favo[1:]
            check_student = 0
            for k in range(4):
                    zx = i + dx[k]
                    zy = j + dy[k]
                    if (0 <= zx < n and 0 <= zy < n):
                        # 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다
                        if (graph[zx][zy] in fav):
                            check_student += 1
            if check_student==1:
                    find+=1
            elif check_student==2:
                    find+=10
            elif check_student==3:
                    find+=100
            elif check_student==4:
                    find+=1000
            ind+=1
    return find


total=dict()
for l in favorite:
    temp = l
    num = temp[0]
    favorite_student = temp[1:]

    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다

    check = []
    check = check_favorite(check, favorite_student)

    if (len(check) == 1):
        a1, a2 = check[0]
        graph[a1][a2] = num
        total[num]=(a1,a2)
    else:
        # 인접한 칸 중에서 비어 있는 칸이 가장 많은 칸으로 자리 정하기
        next = []
        next = check_empty(check)
        if(len(next)==1):
            a1, a2 = next[0]
            graph[a1][a2] = num
            total[num] = (a1, a2)
        else:
            #만족하는 칸이 여러개일 경우 행의 번호가 가장 작은 칸
            #그러한 칸도 여러개이면 열의 번호가 가장 작은 칸으로 정한다
            next=sorted(next,key=lambda x:(x[0],x[1]))
            a1, a2 = next[0]
            graph[a1][a2] = num
            total[num] = (a1, a2)

print(last_cal(total,favorite))