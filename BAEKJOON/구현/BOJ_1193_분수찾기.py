import sys

input = sys.stdin.readline

n = int(input())

line = 1
while n > line:  # 6 > 1
    n -= line  # 5
    line += 1  # 2

if line % 2 == 0:  # 0
    a = n  # a = 5
    b = line - n + 1  #
else:
    a = line - n + 1
    b = n

print(a, '/', b, sep='')

# array = []
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         array[i][j].append([str(i) + '/' + str(j)])
#
# dx = [0, 1, 1, -1]
# dy = [0, -1, 0, 1]
#
# print(array[1][1])
# print(array[1][2])

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         dx = array[i][j] + dx[i]
#         dy = array[i][j] + dy[i]
#
# print(*array[dx][dy])
