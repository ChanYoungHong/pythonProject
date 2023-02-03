import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

sum = [sum(nums[:m])]

for i in range(n - m):
    sum.append(sum[i] - nums[i] + nums[m+i])

print(max(sum))