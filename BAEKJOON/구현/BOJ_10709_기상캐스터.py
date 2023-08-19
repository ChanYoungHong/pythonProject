import sys

input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]


t_cloud = 0
is_cloud = False


for i in range(n):
    for j in range(m):

        if board[i][j] == 'c':
            board[i][j] = 0
            is_cloud = True
            t_cloud = 1

        elif board[i][j] == '.' and is_cloud == False:
            board[i][j] = -1

        elif board[i][j] == '.' and is_cloud == True:
            board[i][j] = t_cloud
            is_cloud = True
            t_cloud += 1

    t_cloud = 1
    is_cloud = False
    print(*board[i])