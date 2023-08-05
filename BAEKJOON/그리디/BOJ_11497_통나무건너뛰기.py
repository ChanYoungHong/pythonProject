import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = 0

    for i in range(2, a):
        res = max(res, arr[i] - arr[i-2])

    print(res)

