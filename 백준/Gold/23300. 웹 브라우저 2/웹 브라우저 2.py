import sys, copy, heapq
import heapq, math
from itertools import permutations, combinations, product
from collections import deque
from itertools import product
#sys.setrecursionlimit(10 ** 5)
#a=list(product(i,repeat=len(powers)))
#b=list(product(*a)) #리스트 안에 있는 원소들끼리 조합




from itertools import combinations_with_replacement as cwr
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
back = deque()
front = deque()
count = 0

# 압축 기능은 뒤로가기 공간에 들어올시에 처리를 해준다고 생각하면됨
now = -1  # 현재 보고 있는 페이지를 의미함
for _ in range(m):
    c = list(map(str, input().split()))
    if (len(c) == 1):
        if c[0] == "B":  # 뒤로가기
            if len(back) >= 1:
                front.appendleft(now)

                now = back.pop()

        elif c[0] == "F":  # 앞으로 가기
            if len(front) > 0:
                back.append(now)

                now = front.popleft()
        elif c[0] == "C":  # 압축하기
            ui = deque()
            k = 0

            while (k < len(back)):
                if (k+1<len(back) and back[k] == back[k + 1]):
                    l=k
                    count=1
                    while l+1<len(back):
                        if(back[l]==back[l+1]):
                           count+=1
                        else:
                            break
                        l+=1
                    ui.append(back[k])
                    l+=1
                    k =l
                else:
                    ui.append(back[k])
                    k += 1

            back = ui


    else:  # 웹페이지 접속
        if count == 0:
            front = deque()
            now = int(c[1])
            count += 1
        else:
            back.append(now)
            front = deque()
            now = int(c[1])

            # 이제 back에 넣어줄시에 중복된 얘들이 있다면 제거해 주는 작업을 하자
print(now)
if (len(back) > 0):
    back.reverse()
    print(*back)
else:
    print(-1)
if (len(front) > 0):
    # back.reverse()
    print(*front)
else:
    print(-1)