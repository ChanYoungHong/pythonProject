import sys

input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (m+1) for _ in range(n+1)]




for i in range(n):
    for j in range(m):

        dp[i][j] = arr[i][j] + max(dp[i-1][j], dp[i][j-1])


# for i in range(n+1):
#     for j in range(m+1):
#
#         print(dp[i][j], end = ' ')
#     print()

print(dp[n-1][m-1])