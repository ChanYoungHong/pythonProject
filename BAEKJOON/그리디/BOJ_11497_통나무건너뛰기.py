import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):

    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    res = 0
    for j in range(2, n):
        res = max(res, abs(arr[j] - arr[j-2]))

    print(res)