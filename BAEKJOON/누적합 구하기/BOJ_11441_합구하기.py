import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0]
summ = 0

for j in range(n):

    summ += arr[j]
    dp.append(summ)

# print(dp)

m = int(input())
for i in range(m):

    a,b = map(int, input().split())
    res = (dp[b] - dp[a-1])
    print(res)