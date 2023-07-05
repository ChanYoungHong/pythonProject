import sys

input = sys.stdin.readline

'''
1. 아이디어 - 20000 사이라서 nlongn 써야해서 이진탐색으로 접근
2. 시간복잡도 - 20000 사이라서 nlongn 써야해서 이진탐색으로 접근
3.

이진탐색 알고리즘 특징 - 
이진 탐색이란 데이터가 정렬돼 있는 배열에서 특정한 값을 찾아내는 알고리즘이다.

'''

t = int(input())

aarr = []
barr = []

def bs(arr, start, end, target):

    res = -1
    while start <= end:

        mid = (start + end) // 2

        if arr[mid] < target:
            res = mid
            print('res : ', res)
            start = mid + 1
        else:
            end = mid - 1
    return res


for _ in range(t):
    a,b = map(int, input().rstrip().split())

    aarr = list(map(int, input().split()))
    barr = list(map(int, input().split()))

    barr.sort()
    cnt = 0

    for i in aarr:
        cnt += bs(barr, 0, len(barr) - 1, i) + 1
        print('bs(barr, 0, len(barr) - 1, i) :', bs(barr, 0, len(barr) - 1, i))

    print(cnt)




