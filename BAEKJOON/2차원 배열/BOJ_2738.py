# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
#
# array = []
#
# for _ in range(n * 2):
#     array.append(list(map(int, input().split())))
#
# answer = [[0] * (m) for _ in range(n * 2)]
#
# for i in range(3):  # 0 1 2
#     for j in range(m):  # j = 0 1 2
#         if i == 0:
#             answer[i][j] += array[0][j] + array[3][j]
#         elif i == 1:
#             answer[i][j] += array[1][j] + array[4][j]
#         elif i == 2:
#             answer[i][j] += array[2][j] + array[5][j]
#         print(answer[i][j],  end=' ')
#     print()


import sys
input = sys.stdin.readline

n,m = map(int,input().split())
array1 = []
array2 = []

for i in range(n):
    array1.append(list(map(int, input().split())))

for i in range(n):
    array2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        array1[i][j] += array2[i][j]

for i in array1:
    print(*i)