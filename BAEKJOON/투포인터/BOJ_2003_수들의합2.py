'''

n < 10,000 보다 작으니깐 투 포인터가 적합 함

'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

inter_sum = 0
end = 0
cnt = 0

for i in range(n):

    while inter_sum < m and end < n:

        inter_sum += nums[end]
        end += 1

    if inter_sum == m:
        cnt += 1

    inter_sum -= nums[i]

print(cnt)
