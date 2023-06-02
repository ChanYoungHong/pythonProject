import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):

        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

order = max(dp)
res = []
for i in range(n-1, -1, -1):

    if dp[i] == order:
        order -= 1
        res.append(nums[i])

res.sort()
print(*res)







