import sys
from collections import deque

input = sys.stdin.readline

'''

1. 바이러스 상 하 좌 우 움직임
2. 낮은 종류의 바이러스부터 먼저 증식한다
3. 이미 존재하면 못 들어감 ( visited로 처리)
4. 


'''

dx = [-1,1,0,0]
dy = [0,0,-1,1]
virus = []

n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] != 0:
            virus.append((board[i][j], i, j, 0))

s, rx, ry = map(int, input().split())
visited = [[False] * n for _ in range(m)]

virus.sort()
q = deque(virus)
def bfs():

    while q:

        virus, x, y, sec = q.popleft()

        if sec == s:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # bfs(nx,ny, sec + 1)
                # visited[nx][ny] = True

                if board[nx][ny] == False:
                    board[nx][ny] = virus
                    q.append((virus, nx,ny, sec+1))

    return board[rx-1][ry-1]


print(bfs())