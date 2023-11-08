import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = int(input())


arr.sort()
start = 0
end = len(arr) - 1
cnt = 0

while start < end:

    if arr[start] + arr[end] > ans:
        end -= 1
    elif arr[start] + arr[end] < ans:
        start += 1
    else:
        cnt += 1
        start += 1
        end -= 1


print(cnt)