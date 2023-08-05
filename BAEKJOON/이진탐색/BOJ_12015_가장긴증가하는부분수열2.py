import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0]

for i in range(n):

    start = 0
    end = len(dp) - 1

    while start <= end:

        mid = (start + end) // 2

        if dp[mid] < arr[i]:
            start = mid + 1
        else:
            end = mid - 1

    if start >= len(dp):
        dp.append(arr[i])
    else:
        dp[start] = arr[i]

print(len(dp) - 1)
