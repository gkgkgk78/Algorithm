def find(total,ch):
    for i in range(4):
        for j in range(3):
            if total[i][j]==ch:
                return[i,j]


def solution(numbers, hand):
    answer = ''
    total=[["1","2","3"],["4","5","6"],["7","8","9"],["*","0","#"]]
    lx,ly=3,0
    rx,ry=3,2
    left=[1,4,7]
    right=[3,6,9]
    for i in numbers:
        if i in left:
            lx,ly=find(total,(str)(i))
            answer+="L"
        elif i in right:
            rx,ry=find(total,(str)(i))
            answer+="R"
        else:
            nx,ny=find(total,(str)(i))
            #누가 더 거리가 가까운지 판단하자
            l1=abs(lx-nx)+abs(ly-ny)
            r1=abs(rx-nx)+abs(ry-ny)
            if l1==r1:
                if hand=="right":
                    rx,ry=nx,ny
                    answer+="R"
                else:
                    lx,ly=nx,ny
                    answer+="L"
            elif l1<r1:
                lx,ly=nx,ny
                answer+="L"
            else:
                rx,ry=nx,ny
                answer+="R"
                
    
    
    return answer