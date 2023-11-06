import sys

input = sys.stdin.readline

n,k = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * n
dp = [sum(arr[:k])]


for i in range(n-k):
    dp.append(dp[i] + arr[i+k] - arr[i])

print(max(dp))
