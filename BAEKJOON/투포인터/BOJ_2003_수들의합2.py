import sys

input = sys.stdin.readline

n,m = map(int, input().split())
nums = list(map(int, input().split()))

inter_num = 0
end = 0
cnt = 0


for i in range(n):

    while inter_num < m and end < n:
        inter_num += nums[end]
        end += 1

    if inter_num == m:
        cnt += 1

    inter_num -= nums[i]

print(cnt)
