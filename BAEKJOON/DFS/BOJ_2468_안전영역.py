import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

'''
1. 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개 만들어 지는지
2. 
3.
4. 


'''

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


dx = [1,-1,0,0]
dy = [0,0,-1,1]


def dfs(x,y,h):


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and board[nx][ny] > h:
                visited[nx][ny] = True
                dfs(nx,ny,h)

res = []
for y in range(max(map(max, board))):

    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):

            if board[i][j] > y and not visited[i][j]:
                visited[i][j] = True
                cnt += 1
                dfs(i,j,y)

    res.append(cnt)
    result = max(res)

print(result)
