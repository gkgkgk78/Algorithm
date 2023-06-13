import sys

input = sys.stdin.readline

n, p = map(int, input().split())
e = list(map(str, input().rstrip()))
val = list(map(int, input().split()))  # A C G T
alpa=["A","C","G","T"]
now = dict()  # 현재 포함하고 있는 개수를 파악하기 위한 딕셔너리
#초기 설정 중
for i in alpa:
    now[i]=0

for l in range(p):
    now[e[l]] += 1


left=0
right=p-1
ans=0

def check():
    global ans
    t=0
    for i in alpa:
        ne=now[i]
        if ne<val[t]:
            return
        t+=1
    ans+=1

check()

while right+1<n:
    right+=1
    now[e[right]]+=1
    now[e[left]]-=1
    left+=1
    check()
print(ans)