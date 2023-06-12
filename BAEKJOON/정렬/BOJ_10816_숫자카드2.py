import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
arr1 = list(sorted(map(int, input().split())))

m = int(input())
arr2 = list(map(int, input().split()))


def bs(arr, start, end, target):

    if start > end:
        return 0

    mid = (start + end) // 2

    if arr1[mid] == target:
        return cnt.get(target)
    elif arr1[mid] < target:
        return bs(arr1[mid], mid + 1, end, target)
    else:
        return bs(arr1[mid], start, mid - 1, target)

cnt = {}

for i in arr1:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for j in arr2:
    print(bs(arr1, 0, len(arr1)-1, j), end = ' ')


# z = Counter(arr1)
#
# for k in arr2:
#     print(z[k], end = ' ')
