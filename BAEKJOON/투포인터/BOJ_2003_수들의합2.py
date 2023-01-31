import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

end = 0
inter_sum = 0
cnt = 0

for start in range(n):

    while inter_sum < m and end < n:
        inter_sum += nums[end]
        end += 1

    if inter_sum == m:
        cnt += 1

    inter_sum -= nums[start]

print(cnt)
