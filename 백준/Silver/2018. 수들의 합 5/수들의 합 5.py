import sys

input = sys.stdin.readline

n = int(input())

# nums = []
# cnt = 0
# for i in range(1, n+1):
#     nums.append(i)
#
#     for j in range(i):
#         if (nums[i] + nums[j]) == n:
#             cnt += 1
#
# print(nums)
# print(cnt)

cnt = 0
inter_num = 0
end = 0

for j in range(0, n):

    while inter_num < n and end <= n-1:
        inter_num +=  end + 1
        end += 1

    if inter_num == n:
        cnt += 1

    inter_num -= j + 1

print(cnt)
