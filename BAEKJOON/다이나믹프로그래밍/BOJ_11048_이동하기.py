'''
가장 큰 수로 따라서 들어가야 하는데..
어떻게 큰 수로 들어가서 그 다음 작은 수로 쭉쭉 들어가지 ?

규칙을 먼저 찾기
'''
import sys

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = graph[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

print(dp[n][m])
print(dp[1][1])
print(graph[0][0])
print(graph)
