'''

1. 시간 복잡도 n < 100,000이니깐 nlogn을 사용하기
2.

'''

import sys

input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

def bs(arr, start, end, target):

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1


for i in arr2:
    if bs(arr1, 0, len(arr1) - 1, i) is not None:
        print(1)
    else:
        print(0)
