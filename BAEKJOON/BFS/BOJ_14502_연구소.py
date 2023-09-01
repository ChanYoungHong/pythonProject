import sys, copy
from collections import deque

'''
벽 1 / 바이러스 2 / 빈칸 0

1. 벽은 세우는 건 브루스 포트로 모든 경우의 수를 다 계산 
2. 바이러스는 퍼져야하니 bfs를 사용해야 함
3. 


'''

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]

result = 0
def makeWall(cnt):

    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):

            if board[i][j] == 0:
                board[i][j] = 1
                makeWall(cnt + 1)
                board[i][j] = 0

def bfs():

    q = deque()
    ex_board = copy.deepcopy(board)

    for i in range(n):
        for j in range(m):

            if board[i][j] == 2:
                q.append((i,j))

    while q:

        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if ex_board[nx][ny] == 0:
                    ex_board[nx][ny] = 2
                    q.append((nx,ny))


    global result
    cnt = 0

    for h in range(n):
        for k in range(m):

            if ex_board[h][k] == 0:
                cnt += 1

    result = max(result, cnt)

makeWall(0)
print(result)