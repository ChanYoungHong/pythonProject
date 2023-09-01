import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

s_x, s_y = 0, 0
eat_cnt = 0
s_size = 2

# 아기상어 위치 좌표 그리고 움직이므로 0으로 초기화
for i in range(n):
    for j in range(n):

        if board[i][j] == 9:
            s_x, s_y = i, j
            board[i][j] = 0


def bfs():
    global s_x, s_y, eat_cnt, s_size

    visited = [[False] * n for _ in range(n)]
    q = deque([(s_x, s_y, 0)])
    candi = []

    while q:

        x, y, time = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] <= s_size:
                    q.append((nx, ny, time + 1))
                    visited[nx][ny] = True

                # 먹을 수 있는 물고기 범위 추가
                if 0 < board[nx][ny] < s_size:
                    candi.append((nx, ny, time + 1))

    # 먹을 수 있는 물고기가 하나도 없을 경우
    if not candi:
        return None

    # 가장 가까운 물고기로 정렬하기
    candi.sort(key=lambda x: (x[2], x[0], x[1]))
    return candi[0]


total_time = 0
while True:
    result = bfs()

    if result is None:
        break

    x, y, time = result
    total_time += time

    # 자신의 크기와 같은 수의 물고리를 먹으면 크기가 1증가 하는 코드
    if eat_cnt == s_size:
        s_size += 1
        eat_cnt = 0

    s_x, s_y = x, y
    board[x][y] = 0

print(total_time)
