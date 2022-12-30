import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    current_color = graph[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n):
            #현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같으면 dfs로 넣어준다.
            if not visited[nx][ny]:
                if graph[nx][ny] == current_color:
                    dfs(nx,ny)

        # if nx < 0 or ny < 0 or nx >= n or ny >= n:
        #     if not visited[nx][ny]:
        #         if graph[nx][ny] == current_color:
        #             dfs(nx, ny)

result = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            result += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

result2 = 0
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            result2 += 1

print(result, result2)


# if graph[x][y] == 'G':
#     graph[x][y] = 0
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         dfs(nx, ny)
#     return True
#
# if graph[x][y] == 'B':
#     graph[x][y] = 0
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         dfs(nx, ny)
#     return True


