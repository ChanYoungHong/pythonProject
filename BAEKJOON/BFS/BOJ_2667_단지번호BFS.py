from collections import deque



n = int(input())
board = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x,y):

    global cnt
    cnt = 1

    q = deque()
    q.append((x,y))

    while q:

        x,y = q.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    q.append((nx,ny))
                    cnt += 1

    return cnt

res = []

for i in range(n):
    for j in range(n):

        # 새로운 영역의 1을 만났을 대 res에 넣음
        if board[i][j] == 1:
            board[i][j] = 0
            res.append(bfs(i,j))


print(len(res))
for i in sorted(res):
    print(i)