import sys

input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

a, b = len(word1), len(word2)
dp = [[0] * (b + 1) for _ in range(a + 1)]

for i in range(1, a + 1):
    for j in range(1, b + 1):
        if word1[i - 1] == word2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[-1][-1])
