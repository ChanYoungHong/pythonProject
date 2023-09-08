import sys

input = sys.stdin.readline

'''
남북방향 - H 킬로
동서방향 - W 킬로미터

모든 구름음 1분이 지날 때 -> 1킬로씩 동쪽으로 이동

구름이 있을 때 -> c
구름이 없을 때 -> . 

무슨 기준으로 시간을 매기나.. ?
'''

n,m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]


is_cloud = False
t_cloud = 0

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