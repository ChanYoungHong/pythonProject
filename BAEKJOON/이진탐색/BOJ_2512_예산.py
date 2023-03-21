import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
temp = []
start = 1
end = max(nums)


standard = m // n

for i in nums:
    if i >= standard:
        temp.append(i)



while start <= end:
    mid = (start + end) // 2



    if sum(nums)


