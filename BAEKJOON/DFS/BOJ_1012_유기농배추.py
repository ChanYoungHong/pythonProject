import sys
from collections import deque

input = sys.stdin.readline


'''
<point>

1. 배추와 배추 사이를 이동 할 수 있음
2. 최소한 필요한 지렁이 수를 구하여라
3. 0은 배추가 심어져 있지 않은 땅, 1은 배추가 심어져 있는 땅

'''

t = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):

    q = deque()
    q.append((x,y))

    while q:

        x,y = q.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append((nx,ny))

for i in range(t):
    cnt = 0
    m,n, cab = map(int, input().rstrip().split())
    board = [[0] * m for _ in range(n)]

    # m 은 가로,  n은 세로
    for j in range(cab):
        a,b = map(int, input().split())
        board[b][a] = 1

        # if board[a][b] == 0:
        #     board[a][b] = 1
        #     q.append((a,b))

    for z in range(n):
        for k in range(m):

            if board[z][k] == 1:
                bfs(z,k)
                cnt += 1

    print(cnt)





