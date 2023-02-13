import sys

input = sys.stdin.readline

word = input().rstrip()
dp = [0] * 10
for i in word:

    idx = int(i)

    if idx == 6:
        idx = 9

    dp[idx] += 1
dp[9] = (dp[9] + 1) // 2

print(max(dp))