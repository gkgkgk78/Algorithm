import sys,itertools
from itertools import permutations
#sys.stdin = open("input.txt")

# stack=[]
# stack.append(1)
# print(stack) #stack에 삽입
# top=stack.pop()#stack에서의 pop과정
# print(top)
# print(stack)
#top=stack[-1]#스택에서 제거 안하고 그냥 원소만 가져옴


a=int(input())


map = [list(map(int, input().split())) for _ in range(a)]

#print(map)
map.sort()
#print(map)
index=-1
max=-1
last=map[a-1][0]
for i in range(a):
    if map[i][1]>max:
        max=map[i][1]
        index=map[i][0]
#print(index,max)

sum=0
pillar=[0]*(last+1)
for i,h in map:
    pillar[i]=h
#print(pillar)

temp=0
for i in range(index):
    #print(i)
    if pillar[i]>temp:
        temp=pillar[i]
    sum+=temp
#print(sum)
sum+=max
temp=0

for i in range(last,index,-1):
    #print(i)
    if pillar[i]>temp:
        temp=pillar[i]
    sum+=temp

print(sum)




