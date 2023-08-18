import sys

input = sys.stdin.readline


'''
1. 구름이 1분 지날 때마다 1키로씩 이동한다
2. 

'''

n,m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

t_cloud = 1
is_cloud = False

for i in range(n):
    for j in range(m):

        if board[i][j] == 'c':
            board[i][j] = 0
            t_cloud = 1
            is_cloud = True
        elif board[i][j] == '.' and is_cloud == False:
            board[i][j] = -1

        elif board[i][j] == '.' and is_cloud == True:
            board[i][j] = t_cloud
            t_cloud += 1

    is_cloud = False
    t_cloud = 1
    print(*board[i])







