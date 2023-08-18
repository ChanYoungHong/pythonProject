import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, depth):
    global answer

    if depth == k and x == 0 and y == c - 1:
        answer += 1
    else:

        board[x][y] = 'T'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == '.':
                board[nx][ny] = 'T'
                dfs(nx, ny, depth + 1)
                board[nx][ny] = '.'


r, c, k = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
answer = 0
dfs(r-1,0,1)
print(answer)
