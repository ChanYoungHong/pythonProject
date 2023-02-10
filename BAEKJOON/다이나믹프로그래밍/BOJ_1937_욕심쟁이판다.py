import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

result = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y):

    '''방문한 적이 있다면 해당 값을 그대로 가져온다.'''
    if dp[x][y]:
        return dp[x][y]

    '''첫 방문 시 해당 위치는 무조건 먹을 수 잇으므로 1로 설정'''
    dp[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[x][y] < graph[nx][ny]:
                dp[x][y] = max(dp[x][y], dfs(nx,ny) + 1)

    return dp[x][y]


for i in range(n):
    for j in range(n):

        result = max(result, dfs(i,j))

print(result)


