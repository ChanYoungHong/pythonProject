import sys
from collections import deque

input = sys.stdin.readline

'''
<point>

1. 한 칸에 한 마리
2. 8개의 방향
3. 어디서부터 시작하는데 ?3
4. 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다
5. 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수다
6. 브루트 포스로 0의 위치에 다 넣은 다음에 그 1과의 거리를 모두 계산해서 최대값 구하면 안 되나?
7. 그러면 그 거리를 어떻게 구할래 ?
8. 거리를 전부 다 계산 ? 빼거나 더해서 모두 거리저장소에 담아서 최대값을 구하기

9. 핵심 포인트 역으로 아기상의 기준으로 계산하여 볼 것.                                                  

'''

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
q = deque()

def bfs():

    while q:

        x,y = q.popleft()

        for i in range(8):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


for i in range(n):
    for j in range(m):

        if graph[i][j] == 1:
            q.append((i,j))

bfs()
print(max(map(max, graph)) - 1)