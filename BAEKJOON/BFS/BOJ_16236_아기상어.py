'''
1. 시간복잡도 : bfs를 써서 아무렇게나 짜면 됨, 왜 bfs를 써야하나 ?
2. 아이디어 : 조건 그대로 코드를 짜면 될 듯 ..
더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
'''

'''

1 추가적인 디테일 -> 아기상어가 먹은 후에는 그 자리는 0이 되어야 함.
2 일단 물고기가 있는지 없는지 확인을 해야 함

'''
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
babyshark = 2
dist = 0
move_num = 0
eat = 0

INF = sys.maxsize

size = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 추가
sx, sy = 0,0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            sx, sy = i, j
            break

        # if graph[i][j] == 0:
        #     print(0)
        #     # 종료 시키기
        # elif graph[i][j] == 9:
        #     q.append((i, j))
def bfs():

    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * n for _ in range(n)]
    flag = 1e9
    fish = []

    while q:
        global babyshark, dist, move_num, move, eat

        x, y, count = q.popleft()

        if count > flag:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] > size or visited[nx][ny]:
                continue

            ''' 아기상어 레벨이 2이라는 것을 표시를 해줘야 함.. 어떻게 함 ? '''

            if graph[nx][ny] != 0 and graph[nx][ny] < size:
                fish.append((nx, ny, count+1))
                flag = count
            visited[nx][ny] = True
            q.append((nx,ny,count + 1))

            # elif graph[nx][ny] == babyshark:
            #     '''지나가는 것을 어떻게 표현 함 ?? '''
            # elif graph[nx][ny] > babyshark:
            #     continue

    if len(fish) > 0:
        fish.sort()
        x, y, move = fish[0][[0], fish[0][1], fish[0][2]
        move_num += move
        eat += 1
        graph[0][0] = 0
