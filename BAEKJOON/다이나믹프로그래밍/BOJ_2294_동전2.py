import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]

dp = [10001] * (m+1)
dp[0] = 0

for i in nums:
    for j in range(i, m+1):
        if dp[j] > 0:
            dp[j] = min(dp[j], dp[j-i]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])

