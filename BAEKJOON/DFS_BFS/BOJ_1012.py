from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

def bfs(graph, x, y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if x < 0 or y < 0 or nx >= x or ny >= y:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
    return


for i in range(t):
    cnt = 0
    a, b, c = map(int, input().split())
    graph = [[0] * b for _ in range(a)]

    for j in range(c):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(a):
        for j in range(b):
            if graph[x][y] == 1:
                bfs(graph, x, y)
                cnt += 1
    print(cnt)

