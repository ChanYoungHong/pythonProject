
import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [0] * (n+1)
# summ = [sum(nums[:2])]
#
# for i in range(n-2):
#     summ.append(summ[i] - nums[i] + nums[i+2])
#
# print(max(summ))

summ = [nums[0]]

for i in range(n-1):
    summ.append(max(summ[i]+nums[i+1], nums[i+1]))

print(max(summ))
print(summ)




