'''

1. 팔린 티켓의 젤 큰 수만큼의 배열을 하나 만들어서
2.

'''

#
import sys

input = sys.stdin.readline

n = int(input())

soldTicket = list(map(int, input().split()))
totalTicket = []

soldTicket.sort()

for i in range(1, max(soldTicket) + 1):
    totalTicket.append(i)

for j in range(len(soldTicket) + 1):
    if totalTicket[j] != soldTicket[j]:
        print(totalTicket[j])
        break


# import sys
# n=int(sys.stdin.readline())
# nums=sorted(list(map(int, sys.stdin.readline().split())))
# is_full=1
# for i in range(len(nums)):
#     if (i+1)!=nums[i]:
#         print(i+1)
#         is_full=0
#         break
# if is_full == 1:
#     print(n+1)
