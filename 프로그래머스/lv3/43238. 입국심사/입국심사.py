
import sys, copy, heapq
import heapq, math
from queue import PriorityQueue
from itertools import permutations, combinations, product
from collections import deque
from itertools import product

#sys.setrecursionlimit(10 ** 5)
#a=list(product(i,repeat=len(powers)))
#b=list(product(*a)) #리스트 안에 있는 원소들끼리 조합
#sys.stdin = open("input.txt","r")

from itertools import combinations_with_replacement as cwr
from collections import Counter
input = sys.stdin.readline



def binary(left, right, times, n):
    cnt = 0
    answer = -1

    while left <= right:
        mid = int((left + right) / 2)
        cnt = 0
        for i in times:
            cnt += int(mid / i)
        if cnt < n:

            left = mid + 1
        else :
            right = mid - 1

    return left


def solution(n, times):
    times.sort()
    left = 0
    right = times[-1]*n
    answer = binary(left, right, times, n)

    return answer










































