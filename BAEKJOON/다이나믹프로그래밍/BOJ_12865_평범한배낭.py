import sys
from collections import deque

n, m = map(int, input().split())

nums = []
for _ in range(n):
    w, v = map(int, input().split())
    nums.append((w,v))

dp = [[0]*(len(nums[0])) for _ in range(n)]

for i in range(n):
    for j in range(len(nums[0])):
        dp[m] = dp[i-2][0] + dp[i-1][0]

print(nums)
# print(dp[m])



