import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# a1 = []
# for i in range(n):
#     a1.append(input().rstrip())
#
# a2 = []
# for i in range(m):
#     a2.append(input().rstrip())
#
# a1.sort()
# a2.sort()
#
# def bs(start, end, target):
#
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if a1[mid] == target:
#             return True
#         elif a1[mid] < target:
#             start = mid + 1
#         elif a1[mid] > target:
#             end = mid - 1
#
#     return False
#
# res = []
# for i in a2:
#     if bs(0, len(a1)-1, i):
#         res.append(i)
#
# res.sort()
# print(len(res))
# for z in res:
#     print(z)


