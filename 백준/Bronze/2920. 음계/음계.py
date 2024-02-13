import sys

input = sys.stdin.readline


nums = list(map(int, input().split()))

asc_nums = [1,2,3,4,5,6,7,8]
dsc_nums = sorted(asc_nums, reverse=True)


if nums == asc_nums:
    print('ascending')
elif nums == dsc_nums:
    print('descending')
else:
    print('mixed')