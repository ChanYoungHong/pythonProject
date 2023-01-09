'''

1. 0으로 시작하면 안 됨
2. 1이 연속으로 이어지면 안 됨

'''

import sys

input = sys.stdin.readline
#
# n = int(input())
#
# cntArray = []
# result = []
# for i in range(n):
#
#     if i == 0:
#         result += '1'
#     else:
#         result += '0'
# cntArray.append(result)
#
# print(result)
# print(len(cntArray))
# print(cntArray)

s = [0, 1, 1]
for i in range(3, 91):
  s.append(s[i - 2] + s[i - 1])
n = int(input())
print(s[n])