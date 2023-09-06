import sys

input = sys.stdin.readline

n,k = map(int, input().split())

coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

# n = int(input())
# dp = [0] * 100001

dp = [0] * (k+1)

# for i in coins:
#     for j in range(6, 100001):
#
#         dp[]


# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[4] = 7
# dp[5] = 12

# for i in range(6, 100001):
#     dp[i] = (dp[i-3] + dp[i-2] + dp[i-1])
#
# print(dp[n])
#


dp[0] = 1

# (1, 2, 5)
for i in coins:

    # 1 ~ 11 -> 1 2 3 4 5 6 7 8 9 10
    # 2 ~ 11 -> 2 3 4 5 6 7 8 9 10
    # 5 ~ 11 -> 5 6 7 8 9 10
    # j는 i ~ k까지의 금액을 의미한다.
    for j in range(i, k+1):

        if j - i >= 0:
            dp[j] += dp[j-i]
            print('dp[j] : ', dp[j], j)
            print('dp[j-i] : ', dp[j-i], j-i)

print(dp[k])
print(dp)
