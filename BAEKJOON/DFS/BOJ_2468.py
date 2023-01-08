import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, dep):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if graph[nx][ny] > dep and visited[nx][ny] == False:
            visited[nx][ny] = True
            dfs(nx, ny, dep)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = 1
for k in range(max(map(max, graph))):
    visited = [[False] * n for _ in range(n)]
    safe = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                safe += 1
                visited[i][j] = True
                dfs(i, j, k)
    ans = max(ans, safe)

print(ans)
