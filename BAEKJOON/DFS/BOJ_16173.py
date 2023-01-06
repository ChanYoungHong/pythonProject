# 움직이는 거리가 그 자리에 해당하는 숫자만큼 움직이는데
# 그 움직이는 발걸음 개수를 계산을 따로 안 해줘도 되는건지 ? 궁금

import sys

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n or visited[x][y] == True:
        return

    if graph[x][y] == False:
        visited[x][y] = True
        return

    visited[x][y] = True

    dfs(x + graph[x][y], y)
    dfs(x, y + graph[x][y])


dfs(0, 0)

if visited[-1][-1] == 1:
    print('HaruHaru')
else:
    print('Hing')
