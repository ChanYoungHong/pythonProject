import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n

for i in range(n): # 3
    for j in range(i): # 0 1 2

        if nums[i] > nums[j]:
            print(nums[i], nums[j])
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
