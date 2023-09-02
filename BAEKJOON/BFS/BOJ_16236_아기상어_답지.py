import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

s_x, s_y = 0, 0
eat_cnt = 0
s_size = 2

# 먼저 상어의 위치값 구하기
for i in range(n):
    for j in range(n):

        if sea[i][j] == 9:
            s_x, s_y = i, j
            sea[i][j] = 0


def bfs():
    global s_x, s_y, eat_cnt, s_size

    q = deque([(s_x, s_y, 0)])
    visited = [[False] * n for _ in range(n)]
    candi = []

    while q:

        x, y, time = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:

                # 아기상어보다 작은 경우만 먹을 수 있음
                if sea[nx][ny] <= s_size:
                    visited[nx][ny] = True
                    q.append((nx, ny, time + 1))

                # 후보 물고기 안에 들어갈 기준
                if 0 < sea[nx][ny] < s_size:
                    candi.append((nx, ny, time + 1))

    if not candi:
        return None

    # 물고기가 제일 가까운 순으로 정렬하기
    candi.sort(key=lambda x: (x[2], x[0], x[1]))
    return candi[0]


total_time = 0
while True:

    result = bfs()
    if result is None:
        break

    x,y,time = result
    total_time += time
    eat_cnt += 1

    if eat_cnt == s_size:
        s_size += 1
        eat_cnt = 0

    s_x,s_y = x,y
    sea[x][y] = 0

print(total_time)
