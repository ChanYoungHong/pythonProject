import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))


arr.sort()
cnt = 0
start = 0
end = len(arr) - 1

while start <= end:

    if arr[start] + arr[end] > m:
        end -= 1
    elif arr[start] + arr[end] < m:
        start += 1
    else:
        cnt += 1
        start += 1
        end -= 1

print(cnt)
