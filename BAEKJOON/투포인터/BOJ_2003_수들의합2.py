import sys

input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))


end = 0
inter_num = 0
cnt = 0

# 0 1 2 3
for i in range(n):

    while inter_num < m and end < n:
        inter_num += arr[end]
        end += 1

    if inter_num == m:
        cnt += 1

    inter_num -= arr[i]

print(cnt)


# start = 0
# end = len(arr) - 1
# cnt = 1

# while start < end:
#
#     if arr[start] + arr[end] > m:
#         end -= 1
#     elif arr[start] + arr[end] < m:
#         start += 1
#
#     else:
#         cnt += 1
#         start += 1
#         end -= 1
#
# print(cnt)

