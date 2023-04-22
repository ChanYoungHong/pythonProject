import sys
from collections import deque

input = sys.stdin.readline
'''
1. 번호가 낮은 종류의 바이러스부터 먼저 증식한다.
2. 

'''

n,m = map(int, input().split())

board = []
virus = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]


for i in range(n):
    board.append(list(map(int, input().rstrip().split())))
    for j in range(n):

        if board[i][j] != 0:
            virus.append((board[i][j], i, j, 0))

s,xx,yy = map(int, input().split())
virus.sort()
q = deque(virus)

def bfs():

    while q:
        virus, x, y, time = q.popleft()

        if time == s:
            break


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and  0 <= ny < n:
                if board[nx][ny] == 0:
                    board[nx][ny] = virus
                    q.append((virus, nx, ny, time + 1))

    return board[xx-1][yy-1]

print(bfs())


