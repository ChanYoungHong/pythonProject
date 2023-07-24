import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline

'''
1. 알고리즘 - 
2. 시간복잡도 -
3. 배열 -  
'''

n = int(input())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x,y,h):

    for i in range(4):

        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] > k and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny,h)


res = []
for k in range(max(map(max, board))):

    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):

            if board[i][j] > k and not visited[i][j]:
                visited[i][j] = True
                cnt += 1
                dfs(i,j,k)
    res.append(cnt)
    ans = max(res)


print(ans)
