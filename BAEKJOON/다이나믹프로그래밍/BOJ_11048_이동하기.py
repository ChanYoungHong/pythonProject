import sys

input = sys.stdin.readline

'''
1. 시간복잡도 n < 1000 작으니깐 2중 반복문을 해결하기
2. 가능해보임

'''

n,m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):

        dp[i][j] = board[i-1][j-1] + max(dp[i-1][j], dp[i][j-1])

# print(dp)
print(dp[n][m])