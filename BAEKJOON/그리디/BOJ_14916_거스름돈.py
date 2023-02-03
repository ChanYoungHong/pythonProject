import sys

input = sys.stdin.readline

n = int(input())

dp = [-1] * 100001

dp[5] = 1
dp[4] = 2
dp[2] = 1

for i in range(6, n+1):

    if i % 5 == 0:
        dp[i] = dp[i-5] + 1
    elif i % 2 == 0:
        dp[i] = dp[i-2] + 1
    elif dp[i-2] > 0 and dp[i-5] > 0:
        dp[i] = min(dp[i-2], dp[i-5]) + 1

if dp[n] < 0 and n < 0:
    print(-1)
else:
    print(dp[n])
