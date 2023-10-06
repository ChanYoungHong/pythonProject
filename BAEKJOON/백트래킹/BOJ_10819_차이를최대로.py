import sys
from itertools import permutations

input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))

res = 0
for per in permutations(arr):

    tmp = 0
    for i in range(n-1):
        tmp += abs(per[i] - per[i+1])
    res = max(res, tmp)

print(res)
