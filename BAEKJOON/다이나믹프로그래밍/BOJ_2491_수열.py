import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [[1] * n for _ in range(2)]

# num = list(map(int, input().split()))
# d = [[1] * n for _ in range(2)]

for i in range(n-1):

    if nums[i] <= nums[i+1]:
        dp[0][i+1] = dp[0][i] + 1
    if nums[i] >= nums[i+1]:
        dp[1][i+1] = dp[1][i] + 1

print(max(map(max, dp)))
#
# for i in range(1,n):
#     if num[i-1]<=num[i]: #증가할경우
#         d[0][i] = d[0][i-1]+1
#     if num[i-1]>=num[i]: #감소할경우
#         d[1][i] = d[1][i-1]+1
# print(max(map(max,d)))
# print(d)