import sys
sys.setrecursionlimit(10000)  # 예: 최대 재귀 호출 스택 깊이를 10000으로 설정
from collections import deque

'''
1. 알고리즘 - BFS를 사용하기 + 
1-1 정상인인 경우 1개
1-2 적록색약인 경우 1개

2. 시간복잡도 - O(V+E)
3. 배열 - 
'''
input = sys.stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

cnt1, cnt2 = 0,0

def dfs(x,y):

    global cnt1, cnt2

    current_color = board[x][y]

    for i in range(4):

        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and current_color == board[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny)


res = []

for i in range(n):
    for j in range(n):

        if visited[i][j] == False:
            visited[i][i] = True
            dfs(i,j)
            cnt1 += 1
res.append(cnt1)

# 적록색약 병이 있을 경우에 다시 바꿔주기
for i in range(n):
    for j in range(n):

        if board[i][j] == 'G':
            board[i][j] = 'R'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):

        if visited[i][j] == False:
            visited[i][j] = True
            dfs(i,j)
            cnt2 += 1
res.append(cnt2)

print(*res)
