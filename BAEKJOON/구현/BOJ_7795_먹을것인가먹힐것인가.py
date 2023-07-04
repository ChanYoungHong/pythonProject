import sys

input = sys.stdin.readline

t = int(input())


def bs(arr, start, end, target):
    res = -1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return res


for i in range(t):

    a, b = map(int, input().split())

    aarr = list(map(int, input().split()))
    barr = list(map(int, input().split()))
    cnt = 0
    aarr.sort()
    barr.sort()

    for j in range(a):
        cnt += bs(barr, 0, len(barr) - 1, aarr[j]) + 1

    print(cnt)
