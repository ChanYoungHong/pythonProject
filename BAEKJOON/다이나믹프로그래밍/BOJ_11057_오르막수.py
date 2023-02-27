import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 10
dp[0] = 1

for i in range(1, n+1):
    for j in range(1, 10):

        dp[j] += dp[j-1]

print(sum(dp) % 10007)
