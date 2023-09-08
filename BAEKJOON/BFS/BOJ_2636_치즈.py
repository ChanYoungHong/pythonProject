import sys
from collections import deque

input = sys.stdin.readline

'''
1. 시간과 녹기 한 시간 전에 남아있는 치즈조각이 몇 개인지 구하라
2. c로 표시되어 있는 부분만 한 시간 후에 녹아 없어진다.
3. c로 표시되어 있는 애들의 기준을 어떻게 정하면 좋을까 ??? -> 
4. c를 만드는 기준은 공기중에 2개 이상 표현이 붙어 있으면 c로 간주한다

'''

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

time = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
ans = []

# c로 표시되어 있는 애들을 일단 q에 넣어야 함
def bfs():

    q = deque()
    q.append((0,0))

    visited[0][0] = 1
    cnt = 0

    while q:

        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:

                if board[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1

                elif board[nx][ny] == 1:
                    board[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1

    ans.append(cnt)
    return cnt


time = 0
while 1:

    time += 1
    visited = [[0] * m for _ in range(n)]
    cnt = bfs()

    if cnt == 0:
        break

print(time-1)
print(ans[-2])