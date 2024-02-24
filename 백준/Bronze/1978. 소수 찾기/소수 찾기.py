import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# cnt = 0
# for i in nums:
#     if i == 2 or i == 3:
#         cnt += 1
#     elif (i%2) == 1 and (i%3) == 1:
#         cnt += 1
#     elif (i%2) == 1 and (i%3) != 0:
#         cnt += 1
#     elif (i%2) != 0 and (i%3) == 1:
#         cnt += 1
#
# print(cnt)

cnt = 0

for num in nums:
    error = 0

    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1

        if error == 0:
            cnt += 1

print(cnt)