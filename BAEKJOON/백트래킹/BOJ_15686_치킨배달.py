from itertools import combinations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):

        if board[i][j] == 1:
            house.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))

res = 1e9
for i in combinations(chicken, m):
    temp = 0

    for hx,hy in house:
        mini = 1e9

        for cx, cy in chicken:
            mini = min(mini, abs(hx-cx) + abs(hy-cy))
        temp += mini
    res = min(res, temp)

print(res)