import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split())) # 5 4 3 2 1

sum = 0
ch_nums = [0]

for i in range(n):
  sum += nums[i]
  ch_nums.append(sum)

result = 0
for i in range(m):
  a, b = map(int, input().split())
  result = ch_nums[b] - ch_nums[a-1]
  print(result)
