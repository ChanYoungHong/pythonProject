

'''

시간복잡도 - n < 1,000,000 아래이니깐 nlongn을 사용해야 함, 이진탐색

'''
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
start, end = 1, max(nums)

while start <= end:

    mid = (start + end) // 2
    total = 0

    for i in nums:
        if i > mid:
            total += i-mid

    if total >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)