import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

array = set()
answer = 0

def dfs(x, y, cnt):

    global answer
    answer = max(answer, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny] in array:
            array.add(graph[nx][ny])
            dfs(nx,ny, cnt + 1)
            array.remove(graph[nx][ny])



array.add(graph[0][0])
dfs(0, 0, 1)
print(answer)