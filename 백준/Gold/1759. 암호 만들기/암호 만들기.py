import sys,itertools
#sys.stdin = open("input.txt")
from itertools import combinations #순열 함수

a,b=map(int,input().split())

per=input().split()
per.sort()
vowels = ['a', 'e', 'i', 'o', 'u']
for e in combinations(per,a):
    count=0
    jk=0
    count1=0
    for i in range(0,len(e)):
        for j in range(0,len(vowels)):
            if e[i]==vowels[j]:
                count=count+1
                jk=1
        if jk==0:
            count1=count1+1
        else: jk=0

    if count>0 and count1>1:
        print("".join(map(str, e)))


