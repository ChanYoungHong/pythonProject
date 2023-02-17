import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (m + 1) for i in range(n + 1)]

for i in range(n):
    for j in range(m):

        dp[i][j] = graph[i][j] + max(dp[i - 1][j], dp[i][j - 1])

print(dp[n-1][m-1])
