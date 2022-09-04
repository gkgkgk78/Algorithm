import sys,itertools
#sys.stdin = open("input.txt")

from itertools import permutations #순열 함수

N=int(input())
data = list(map(int, input().split()))
kn=0
sum=0


per=itertools.permutations(data,N)

for i in list(per):
    kn=0
    for j in range(0,N-1):

        kn+=abs(i[j]-i[j+1])

    if kn>sum:
        sum=kn


print(sum)