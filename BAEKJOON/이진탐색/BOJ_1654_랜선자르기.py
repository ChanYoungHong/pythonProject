import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lan = [int(input()) for _ in range(n)]
start, end = 1, max(lan)

while start <= end:

    mid = (start + end) // 2
    lines = 0

    for i in lan:
        if i >= mid:
            lines += (i // mid)

    if lines >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
