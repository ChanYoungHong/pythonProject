import sys

input = sys.stdin.readline

n, m = map(int,input().split())
dp = [0] * (m+1)
dp[0] = 1

coins = []
for _ in range(n):
    a = int(input())
    coins.append(a)

for coin in coins:
    for i in range(coin, m+1):

        if i - coin >= 0:
            dp[i] += dp[i-coin]

print(dp[m])