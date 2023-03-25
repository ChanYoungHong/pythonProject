import sys

input = sys.stdin.readline

t = int(input())

dp = [0] * 100

for i in range(t):
    n = int(input())

    dp[n] =