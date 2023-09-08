import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):

        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)


order = max(dp)
res = []
for i in range(n-1, -1, -1):

    if dp[i] == order:
        order -= 1
        res.append(arr[i])

res.sort()
print(len(res))
print(*res)
