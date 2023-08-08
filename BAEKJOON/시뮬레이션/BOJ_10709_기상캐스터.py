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
# board = [[0] * m for _ in range(n)]

# graph = []
#
# for i in range(n):
#     a = input().rstrip()
#     graph.append(a)
#
# for i in range(n):
#     for j in range(m):
#
#         if graph[i][j] == 'c':
#             board[i][j] = 0
#         elif graph[i][j] == '.':
#             board[i][j] = -1
#
# move = 0
# for i in range(n):
#     for j in range(m-1):
#
#         if board[i][j] == move and move == n:
#             board[i][j+1] = board[i][j] + 1
#             move += 1
#
# print(board)

board = [list(input().rstrip()) for _ in range(n)]

cloud_time = 1
is_cloud = False

for i in range(n):
    for j in range(m):


        if board[i][j] == 'c':
            board[i][j] = 0
            is_cloud = True
            cloud_time = 1

        elif board[i][j] == '.' and is_cloud == False:
            board[i][j] = -1

        elif board[i][j] == '.' and is_cloud == True:
            board[i][j] = cloud_time
            cloud_time += 1

    cloud_time = 1
    is_cloud = False
    print(*board[i])