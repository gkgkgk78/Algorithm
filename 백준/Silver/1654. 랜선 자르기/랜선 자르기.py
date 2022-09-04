import sys
input = sys.stdin.readline

N, M = map(int,input().split()) # 나무 수, 필요한 나무 길이
trees = [int(sys.stdin.readline()) for _ in range(N)]

start, end = 1, max(trees) # 시작 점, 끝점
tt=0
# 이분 탐색
while start <= end:
    mid = (start+end)//2
    tree = 0 # 잘린 나무 합
    for i in trees:

            to=i//mid
            tree=tree+to

    if tree >=M: # 원하는 나무 높이보다 더 많이 잘렸으면
        start = mid + 1
    else: # 원하는 나무 높이보다 덜 잘렸으면
        end = mid - 1
    if(tree==M):
        if mid>tt:
            tt=mid
    #print(start,mid,end,tree)
print(end)