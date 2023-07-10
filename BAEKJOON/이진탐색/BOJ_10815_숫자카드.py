import sys

input = sys.stdin.readline

'''
1. 아이디어 - 
2. 시간복잡도 - 50만 아래니깐 NlogN 시간 복잡도 안에 들므로 이진 탐색을 사용하기
3. 문법? 

이진 탐색이란 데이터가 정렬돼 있는 배열에서 특정한 값을 찾아내는 알고리즘이다. 

'''

n = int(input())
arr1 = list(map(int, input().rstrip().split()))

m = int(input())
arr2 = list(map(int, input().rstrip().split()))

arr1.sort()

def bs(arr, start, end, target):
    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1

# 1 2 3 4 5 6 7

for i in arr2:
    if bs(arr1, 0, len(arr1) - 1, i) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
