import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dukk = list(map(int, input().split()))
start, end = 1, max(dukk)

while start <= end:

    mid = (start + end ) // 2
    line = 0

    for i in dukk:
        if i > mid:
            line += i - mid

    if line >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)


