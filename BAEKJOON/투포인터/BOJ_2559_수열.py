import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

temp = [sum(nums[:m])]

for j in range(n - m):  # 0 1 2 3 4 5 6 7 8 9
    temp.append(temp[j] - nums[j] + nums[j + m])

print(max(temp))
