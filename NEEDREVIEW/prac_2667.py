### 1번째 풀이

n = int(input())  # 테스트 케이스의 개수임
graph = []  # 지도를 받을 배열
num = []  # ??

# 지도의 테스트케이스를 다 넣음
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우를 다 확인하기 위한 코드
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    # 마이너스 위치 또는 그 벽의 넘으면 False로 리턴한다
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False

count = 0
result = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])

# ====================================================================

### 2번째 풀이

# n의 개수, graph, visited 정의
n = int(input())
graph = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# 상하좌우 이동 설정
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 입력값을 graph에 기입
for i in range(n):
    line = input()
    for j, b in enumerate(line):
        graph[i][j] = int(b)


# dfs 정의
def dfs(x, y):
    global cnt  # cnt를 사용하기 위해 global 선언
    visited[x][y] = True
    if graph[x][y] == 1:
        cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                dfs(nx, ny)


cnt = 0
housing = []

# 정의된 dfs를 가지고 graph를 탐색
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            dfs(i, j)
            housing.append(cnt)
            cnt = 0

# 문제 답 도출
housing.sort()  # 오름차순 정렬
print(len(housing))
for i in housing:
    print(i)

# ====================================================================

### 3번째 풀이

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = []  # 입력받을 그래프를 담을 리스트 선언
result = []  # 결과를 담을 리스트 선언
count = 0

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

# 한 점을 기준으로 (위 아래 왼쪽 오른쪽) 으로 한칸 씩 이동할 좌표 설정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    global count

    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)


# 그래프의 원소가 1일때만 dfs로 집을 방문한다.
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0

result.sort()  # 오름차순으로 정렬
print(len(result))  # 총 단지수 출력
for k in result:  # 각 단지마다 집의 수 출력
    print(k)


# =========================================================================================================================================================


from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []
cnt = 0


def bfs(xPos, yPos):
    count = 1
    q = deque()
    q.append((xPos, yPos))
    graph[xPos][yPos] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))
                    count += 1
    ans.append(count)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)
            cnt += 1

ans.sort()

print(cnt)
for i in ans:
    print(i)

# ====================================================================================================

n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False


count = 0
result = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])