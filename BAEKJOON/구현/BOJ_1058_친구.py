import sys

input = sys.stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

INF = sys.maxsize

# temp = [[INF] * (n + 1) for _ in range(n + 1)]

temp = [[0] * n for _ in range(n)]


for i in range(n):
    for j in range(n):
        for k in range(n):

            if i == j:
                continue

            if board[i][j] == 'Y' or (board[i][k] == 'Y' and board[k][j] == 'Y'):
                temp[i][j] = 1


result = 0

for i in temp:
    print(sum(i))
    break


# print(result)
