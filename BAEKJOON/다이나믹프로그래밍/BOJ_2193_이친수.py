import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

dp[1] = dp[2] = 1
for i in range(3, n+1):
  dp[i] = dp[i-2] + dp[i-1]


print(dp[n])