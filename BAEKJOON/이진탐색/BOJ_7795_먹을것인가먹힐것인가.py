import sys

input = sys.stdin.readline

'''
1. 아이디어 - 20000 사이라서 nlongn 써야해서 이진탐색으로 접근
2. 시간복잡도 - 20000 사이라서 nlongn 써야해서 이진탐색으로 접근
3.

이진탐색 알고리즘 특징 - 
이진 탐색이란 데이터가 정렬돼 있는 배열에서 특정한 값을 찾아내는 알고리즘이다.

A의 크기가 B보다 큰 쌍이 몇 개나 있는지 구하는 프로그램을 만드시오

'''

t = int(input())

def bs(arr, start, end, target):

    res = -1
    while start <= end:
        mid = (start + end) // 2

        # arr2은 arr임  target : arr1 이고
        if arr[mid] < target:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res

# 0 1 2
# 1 3 6
# res = 1
#

for _ in range(t):
    a,b = map(int, input().rstrip().split())

    arr1 = list(map(int, input().split()))

    # 정렬되어 있는 알고리즘에서 특정한 값을 찾을 때
    arr2 = list(map(int, input().split()))

    arr2.sort()
    cnt = 0

    for i in arr1:
        cnt += bs(arr2, 0, len(arr2) - 1, i) + 1

    print(cnt)




