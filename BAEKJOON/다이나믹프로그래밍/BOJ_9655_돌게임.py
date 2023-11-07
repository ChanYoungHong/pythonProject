import sys

input = sys.stdin.readline

n = int(input())

dp = [-1] * (1001)

dp[1] = 1
dp[2] = 0
dp[3] = 1

# 짝수면 CY
# 홀수면 SK
for i in range(n, 1001):

    if dp[i] == 1 or dp[i-3] == 1:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[n] == 1:
    print('SK')
else:
    print('CY')



