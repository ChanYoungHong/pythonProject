'''

시간복잡도 n이 500,000만 보다 작으니깐 이진 탐색을 선택 함 이유는 nlogn 이니깐 1,000,000까지 가능

1. target에 해당하는 수를 상근이 덱에서 개수를 찾아야 하니깐 count 함수를 사용해서 개수를 추출
2.


'''

import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().rstrip())
array1 = list(map(int, input().rstrip().split()))  # 상근이가 가지고 있는 숫자 카드

m = int(input().rstrip())
array2 = list(map(int, input().rstrip().split()))  # 정수 M개의 카드


c = Counter(array1)

for i in array2:

    if i in c:
        print(c[i], end=' ')
    else:
        print(0, end=' ')


# array1.sort()
#
# def bs(array, target, start, end):
#
#     if start > end:
#         return None
#     mid = (start + end) // 2
#
#     if array[mid] == target:
#         return array[start:end+1].count(target)
#     elif array[mid] < target:
#         return bs(array, target, mid+1, end)
#     else:
#         return bs(array, target, start, mid-1)
#
#
# for i in range(len(array2)):
#     z = bs(array1, array2[i], 0, len(array1)-1)
#
#     if z is not None:
#         print(z, end=' ')
#     else:
#         print(0, end=' ')
# c = Counter(array1)
#
# for i in array2:
#     if i in c:
#         print(c[i], end=' ')
#     else:
#         print(0, end=' ')
#
# print(c)
# def bs(start, end, target):
#
#     while start <= end:
#
#         mid = (start + end) // 2
#
#         if mid == target:
#             return True
#         elif array1[mid] < target:
#             start = mid + 1
#         elif array1[mid] > target:
#             end = mid - 1
#
#     return False
#
#
#
#
# arr = []
#
# #
#
# for i in array2:
#
#     if bs(0, len(array2) -1, array1):
#         arr.append(array1.count(i))
#
# print(*arr)



'''
찾아야 하는 값은 ? -> 상근이가 몇 개 가지고 있는지 구하여라
'''



