import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [sum(arr[:m])]

for i in range(n - m):
    dp.append(dp[i] - arr[i] + arr[m+i])

print(max(dp))
