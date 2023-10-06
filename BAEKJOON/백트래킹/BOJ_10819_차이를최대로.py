import sys
# from itertools import permutations
from itertools import combinations

input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))

test = combinations(arr, 4)

for zz in test:
    print(zz)

# res = 0
# for per in permutations(arr):
#
#     tmp = 0
#     for i in range(n-1):
#         tmp += abs(per[i] - per[i+1])
#     res = max(res, tmp)

# print(res)
