import sys

input = sys.stdin.readline

n = int(input())

cnt_nums = []
#
# for _ in range(n):
#     num = int(input())
#     cnt_nums.append(num)
#
#
# check = []
# for j in cnt_nums:
#
#     if cnt_nums.count(j) >= 2:
#         check.append(j)
#
# check = list(set(check))
# check.sort()
# print(check[0])

dict = {}
cnt_nums = []
for i in range(n):

    num = int(input())
    cnt_nums.append(num)
# 
# print(dict)
# print(set(cnt_nums))

for j in cnt_nums:

    if j in dict:
        dict[j] += 1
    else:
        dict[j] = 1

result = sorted(dict.items(),key = lambda x : (-x[1],x[0]))
print(result[0][0])
