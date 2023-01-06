import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [10001] * (k+1)
dp[0] = 0

for c in coins: # 1 5 12
    for i in range(c, k+1):
        if dp[i] > 0:
            dp[i] = min(dp[i], dp[i-c] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])

# for i in range(2, k+1):
#
#     dp[i] = dp[i-1] + 1
#
#     if i%coins[0] == 0:
#         dp[i] = min(dp[i], dp[i // 1] + 1)
#
#     if i%coins[1] == 0:
#         dp[i] = min(dp[i], dp[i // 5] + 1)
#
#     if i%coins[2] == 0:
#         dp[i] = min(dp[i], dp[i // 12] + 1)
#
# print(dp[k])


'''
지금 적힌 코드는 -> 15를 만드는 모든 경우의 수를 구한 것

내가 구해야 할 것은 -> 15를 만드는데 가장 동전을 적게 사용해서 만들어야 함
'''