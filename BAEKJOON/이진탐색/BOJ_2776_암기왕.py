'''

1. 시간 복잡도 N < 1,000,000이니깐 nlogn을 사용해야 함
2. nlogn을 사용하려면 이분 탐색, 다이나믹 프로그래밍을 써야 함
3.

'''

import sys

input = sys.stdin.readline

test = int(input())



def bs(arr, start, end, target):

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for _ in range(test):
    n = int(input())
    arr1 = list(map(int, input().split()))

    m = int(input())
    arr2 = list(map(int, input().split()))

    arr1 = list(set(arr1))
    arr1.sort()

    for k in arr2:
        print(bs(arr1, 0, len(arr1)-1, k))







