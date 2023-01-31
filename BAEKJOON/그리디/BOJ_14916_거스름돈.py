import sys

input = sys.stdin.readline

n = int(input())

cnt = 0

while True:

    if n % 5 == 0:
        cnt += n // 5
        break
    elif n % 2 == 0:
        n -= 2
        cnt += 1
    else:
        n -= 2
        cnt += 1

if n < 0:
    print(-1)
else:
    print(cnt)



# dp = [-1] * 100001
# dp[2] = 1
# dp[5] = 1
#
#
# for i in range(6, n+1):
#
#     if i % 5 == 0:
#         dp[i] = dp[i-5] + 1
#     elif i % 2 == 0:
#         dp[i] = dp[i-2] + 1
#     elif dp[i-2] > 0 and dp[i-5] > 0:
#         dp[i] = min(dp[i-2], dp[i-5]) + 1
#
# print(dp[n])
