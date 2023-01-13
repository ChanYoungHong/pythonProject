'''

1. 팔린 티켓의 젤 큰 수만큼의 배열을 하나 만들어서
2.

'''

import sys
input = sys.stdin.readline

n = int(input())

nums = sorted(list(map(int, input().split())))

is_full = 1
for i in range(len(nums)):
    if (i+1) != nums[i]:
        print(i+1)
        is_full = 0
        break


if is_full == 1:
    print(n+1)