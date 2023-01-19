'''

1. 시간 복잡도 n < 100,000이니깐 nlogn을 사용하기
2.

'''

import sys
input = sys.stdin.readline

n = int(input())
array1 = list(map(int, input().split()))
m = int(input())
array2 = list(map(int, input().split()))

array1 = list(set(array1))
array1.sort()


def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


for i in array2:
    print(binary_search(array1, i))
