import sys

input = sys.stdin.readline

word = input().rstrip()

dp = [0] * 9

for i in word:

    idx = int(i)

    if idx == 9:
        idx = 6

    dp[idx] += 1

dp[6] = (dp[6]+1) // 2

print(max(dp))

