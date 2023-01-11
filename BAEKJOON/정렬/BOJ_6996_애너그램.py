'''

1. 반복문을 두 개 돌려서 하나씩 비교하는 방법으로 생각 함
2. 오른쪽 값을 기준으로 왼쪽 값을 넣었을 때 그 길이가 오른쪽 값의 길이와 같으면 애니그램으로 출

'''

import sys

input = sys.stdin.readline


n = int(input())

for i in range(n):
    t, h = map(str, input().split())

    x = sorted(list(t))
    y = sorted(list(h))

    if x == y:
        print("%s & %s are anagrams." % (t, h))
    else:
        print("%s & %s are NOT anagrams." % (t, h))

# n = int(input())
#
# array = []
# result = []
# for _ in range(n):
#     array.append(list(map(str, input().split())))
#
#
# for i in array[0][1]:
#     for j in array[0][0]:
#         if i == j:
#             result.append(j)
#
# if len(result) == len(array[0][1]):
#     print('blather & reblath are anagrams.')
# else:
#     print('')
#
# print(result)
#
# for i in range(2):
#     for j in range()
#

