import sys
from collections import deque

input = sys.stdin.readline

'''
1. 가장 짧은 다리를 놓아 두 대륙을 연결하고자 한다.
2. 짧은 다리란 ? - 칸의 수가 가장 작은 다리를 말한다.
3. 대륙의 끝 점끼리 값을 구해야 하는 것인가 ?
4. 각 대륙의 끝점에서 시작해서 BFs 퍼져나가서 1에가 가장 빠르게 도착하는 수를 구하기?

다른 사람들의 답안 -> 2가지 방법을 사용
1번 각 섬을 구분한다.
2번 거리 배열을 만들어서 늘려간다 bfs를 두 개 돌려야 함

'''

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 섬 구별하기
def bfs1(x, y):
    global cnt

    q = deque()
    q.append((x, y))

    visited[x][y] = True
    board[x][y] = cnt

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    board[nx][ny] = cnt
                    q.append((nx, ny))

def bfs2(o):

    global answer
    dist = [[-1] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if board[i][j] == o:
                q.append((i,j))
                dist[i][j] = 0

cnt = 1
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):

        if board[i][j] == 1 and not visited[i][j]:
            bfs1(i, j)
            cnt += 1


for i in range(n):
    for j in range(n):
        print(board[i][j], end=' ')
    print()


for i in range(1, cnt):
    bfs2(i)
