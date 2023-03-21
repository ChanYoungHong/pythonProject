'''
1. 수도코드 -> 일단 n만큼 나눠서 나눈 기준의 수로
2. 기준 수보다 크면 따로 배열에 담아서 처리
3. 무슨 기준으로 저 답을 찾을 수 있나 ??
4. 기준보다 큰 수들을 남겨놓고 그것의 평균을 구하면 답이 나오지 않을까..
5.

'''

import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
start = 1
end = max(nums)

# nums.sort()
# print(nums)
#
# standard = m // n
#
# for i in nums:
#     if i < standard:
#         m -= i
# print(m)
#
#
# while start <= end:
#     mid = (start + end) // 2
#
#
# '''127일 찾아야 하는데 무슨 기준으로 찾음 ???? '''
#     # if sum(nums)

while start <= end:

    mid = (start + end) // 2
    total = 0

    for i in nums:
        if i > mid: # 110 > 75
            total += mid
        else:
            total += i

    if total <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)

