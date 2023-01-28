import sys

input = sys.stdin.readline

n = int(input())

dp = [-1] * 100001

dp[2] = dp[5] = 1
dp[4] = 2
dp[6] = 3
dp[7] = 2
dp[8] = 4

for i in range(9, n + 1):
    dp[i] = min(dp[i - 2], dp[i - 5]) + 1

print(dp[n])

# cnt = 0
#
# while True:
#
#     if n % 5 == 0:
#         cnt += n//5
#         break
#     elif n % 2 == 0:
#         n -= 2
#         cnt += 1
#     else:
#         n -= 5
#         cnt += 1
#
# if n < 0:
#     print(-1)
# else:
#     print(cnt)