import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0]
su = 0
for j in range(n):
    su += arr[j]
    dp.append(su)


m = int(input())
for i in range(m):
    a,b = map(int, input().split())
    print(dp[b] - dp[a-1])

