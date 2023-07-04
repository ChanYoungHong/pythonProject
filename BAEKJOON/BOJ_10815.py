import sys

input = sys.stdin.readline

'''
1. 아이디어

2. 시간복잡도 ?
    N이 500,000까지라 이진 탐색을 사용해야 함
3.

'''

# 상근이가 가지고 있는 숫자 카드
n = int(input())
arr1 = list(map(int, input().split()))


# 구분해야 할 정수 카드
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


for i in range(m):

    if bs(arr1, 0, len(arr1) - 1, arr2[i]) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
