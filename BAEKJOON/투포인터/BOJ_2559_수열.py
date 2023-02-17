import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

dp = [sum(nums[:m])]

for i in range(n-m):

    dp.append(dp[i] - nums[i] + nums[m+i])

print(max(dp))