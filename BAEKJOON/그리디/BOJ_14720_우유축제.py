'''


'''

import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if nums[i] == cnt % 3:
        cnt += 1

print(cnt)


