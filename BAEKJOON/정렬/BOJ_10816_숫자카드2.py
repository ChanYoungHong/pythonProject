import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
# arr1 = list(sorted(map(int, input().split())))
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

# def bs(arr, start, end, target):
#     if start > end:
#         return 0
#
#     mid = (start + end) // 2
#
#     if arr[mid] == target:
#         return cnt.get(target)
#     elif arr[mid] > target:
#         return bs(arr, start, mid - 1, target)
#         # end = mid - 1
#     elif arr[mid] < target:
#         return bs(arr, mid + 1, end, target)
#         # start = mid + 1
#
#
# cnt = {}
# for i in arr1:
#     if i in cnt:
#         cnt[i] += 1
#     else:
#         cnt[i] = 1
#
# for i in arr2:
#     print(bs(arr1, 0, len(arr1) - 1, i), end=' ')


z = Counter(arr1)

for i in arr2:
    print(z[i], end=' ')
