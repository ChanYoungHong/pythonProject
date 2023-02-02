
import sys

input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().split()))

dp = [1] * (n+1)

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
order = max(dp)

res = []
for i in range(n-1, -1, -1):
    if dp[i] == order:
        res.append(nums[i])
        order -= 1
res.reverse()

for i in res:
    print(i, end = ' ')




