from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(graph, a, b):
    q = deque()
    q.append((a, b))
    graph[a][b] = 0

    while q:

        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
    return


t = int(input())

for _ in range(t):
    cnt = 0
    # m이 가로, n이 세로
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(m):
        for b in range(n):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1

    print(cnt)
