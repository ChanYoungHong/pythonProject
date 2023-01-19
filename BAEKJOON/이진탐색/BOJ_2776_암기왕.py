'''

1. 시간 복잡도 N < 1,000,000이니깐 nlogn을 사용해야 함
2. nlogn을 사용하려면 이분 탐색, 다이나믹 프로그래밍을 써야 함
3.

'''

import sys

input = sys.stdin.readline

test = int(input())

for i in range(test):
    n = int(input())
    array1 = list(map(int, input().split()))

    m = int(input())
    array2 = list(map(int, input().split()))

    array1 = list(set(array1))
    array1.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return 0


for j in array2:
    print(binary_search(array1, j, 0, n - 1))

# def binary_search(array, target):
#     start = 0
#     end = len(array1) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return 1
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return 0
#
#
# test = int(input())
#
# for i in range(test):
#     n = int(input())
#     array1 = list(map(int, input().split()))
#     m = int(input())
#     array2 = list(map(int, input().split()))
#
#     array1 = list(set(array1))
#     array1.sort()
#
#     for j in array2:
#         print(binary_search(array1, j))
