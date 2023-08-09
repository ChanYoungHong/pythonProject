import sys

input = sys.stdin.readline

'''
1. 갔던 곳은 안 간다고 함
2. 

'''

r, c, k = map(int, input().split())

board = [list(input().rstrip()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 겹치지 않는 방향?을 저장해야 함
answer = 0

def dfs(x,y,dep):

    global answer

    if dep == k and x == 0 and y == c - 1:
        answer += 1


    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == '.':
            board[nx][ny] = 'T'
            dfs(nx,ny, dep + 1)
            board[nx][ny] = '.'


dfs(r-1, 0, 1)
print(answer)