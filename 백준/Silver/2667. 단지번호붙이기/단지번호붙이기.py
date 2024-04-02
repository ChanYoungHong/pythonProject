import sys

input = sys.stdin.readline



n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):

    global cnt

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
            board[nx][ny] = 0
            dfs(nx,ny)
            cnt += 1


    return cnt



cnt = 0
ans = []
for i in range(n):
    for j in range(n):

        if board[i][j] == 1:
            board[i][j] = 0
            ans.append(dfs(i,j))
            cnt = 0

print(len(ans))
ans.sort()
for i in ans:
    print(i+1)
