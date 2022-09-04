import sys
input = sys.stdin.readline

N=int(input()) # 나무 수, 필요한 나무 길이
trees=[]
trees = (input().split())
trees=list(map(int,trees))
start, end = 0, (max(trees)) # 시작 점, 끝점


tt=0
fin=int(input())
# 이분 탐색
while start <= end:
    mid = (start+end)//2
    tree = 0 # 잘린 나무 합
    for i in trees:
            i=int(i)

            if mid>i:
                tree=tree+i
            elif mid<=i:
                tree=tree+mid
   # print(start,mid,end,tree,fin)
    if tree <=fin: # 원하는 나무 높이보다 더 많이 잘렸으면
        start = mid + 1
    else: # 원하는 나무 높이보다 덜 잘렸으면
        end = mid - 1

    #print(start,mid,end,tree)

print(end)