import sys

input = sys.stdin.readline

t = int(input())

dp = [0] * 1000001

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

for i in range(4, 1000001):
    dp[i] = ((dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009)

for i in range(t):
    n = int(input())
    print(dp[n])

#
# def z(n):
#
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 4
#     else:
#         return z(n-3) + z(n-2) + z(n-1)
#
# t = int(input())
#
# for _ in range(t):
#     te = int(input())

#     print(z(te))





# for i in range(t):
#     coins.append(int(input()))

