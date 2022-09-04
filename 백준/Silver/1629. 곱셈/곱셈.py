import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

a,b,c=map(int,(input().split())) # 나무 수, 필요한 나무 길이
t=1


def dac(a,b):
    if b == 1:
        return (a % c)
    temp=dac(a,b//2)
    if b%2==0:
        return(temp*temp)%c
    else:
        return (temp*temp*a)%c


print(dac(a,b))