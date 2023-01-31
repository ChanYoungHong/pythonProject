import sys

input = sys.stdin.readline

n, m = map(int,input().split())
nums = list(map(int, input().split()))

result = []
result.append(sum(nums[:m]))

for i in range(n - m):
    result.append(result[i] - nums[i] + nums[m+i])

print(max(result))

