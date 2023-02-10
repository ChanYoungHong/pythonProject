import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dp = [0] * (m+1)

coins = []
for _ in range(n):
    a = int(input())
    coins.append(a)

dp[0] = 1
for i in coins:
    for j in range(i, m+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

print(dp[m])




