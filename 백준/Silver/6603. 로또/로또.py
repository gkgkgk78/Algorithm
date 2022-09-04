import sys,itertools
from itertools import combinations #순열 함수


while True:
    N, *arr = map(int, input().split())
    if N==0:
        break
    for e in  list(combinations(arr,6)):
        print(*e)
    print()

