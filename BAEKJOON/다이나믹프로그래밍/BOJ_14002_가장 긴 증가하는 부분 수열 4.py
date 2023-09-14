import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):

        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# print(dp)

order = max(dp)
res = []
for z in range(n - 1, -1, -1):

    if order == dp[z]:
        res.append(arr[z])
        order -= 1

print(len(res))
res.sort()
print(*res)
