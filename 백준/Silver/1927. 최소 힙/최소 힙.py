import sys, heapq
from collections import deque

input = sys.stdin.readline

n = int(input())

nums = []

for _ in range(n):

    x = int(input().rstrip())


    if x == 0:
        if len(nums):
            print(heapq.heappop(nums))
        else:
            print(0)
    else:
        heapq.heappush(nums, x)