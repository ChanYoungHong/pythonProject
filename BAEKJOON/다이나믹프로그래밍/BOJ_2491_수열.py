import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [[1] * n for _ in range(2)]

for i in range(n - 1):

    if nums[i] >= nums[i + 1]:
        dp[0][i + 1] = dp[0][i] + 1

    if nums[i] <= nums[i + 1]:
        dp[1][i + 1] = dp[1][i] + 1


print(max(map(max, dp)))