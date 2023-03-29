import sys

input = sys.stdin.readline

t = int(input())

nums = [0]
# print('nums : ', nums)
# nums = [int(input().rstrip()) for _ in range(t)]
for i in range(t):
    nums.append(int(input().rstrip()))
# dp = [0] * (t+1)
# print('nums : 22', nums)
dp = [0]
dp.append(nums[1])

# t가 하나일 경우 다른 nums[2]는 없기 때문에 런타임 인덱스 에러가 간ㅁ
if t > 1:
    dp.append(nums[1] + nums[2])

# 최종값이 더 클 경우 for문에 안 들어감, 그냥 니가감 에러도 안 터짐 신기함
for i in range(3, t+1):
    dp.append(max(dp[i-1], dp[i-3] + nums[i-1] + nums[i], dp[i-2] + nums[i]))

print(dp[t])
print(dp)
print(nums)