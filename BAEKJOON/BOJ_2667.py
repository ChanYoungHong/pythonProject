# n = int(input())
#
# board = [[0] * n for _ in range(n)]
# #visited = [False] * 100 * 100
# visited = [[False] * n for _ in range(n)]
#
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# # 답 보고 추가한 코드
# # 테스트코드 그 지도들 넣는 코드
# # for i in range(n):
# #     board.append(list(map(int, input())))
#
# for i in range(n):
#     line = input()
#     for j, b in enumerate(line):
#         board[i][j] = int(b)
#
# def dfs(x, y):
#     global cnt
#     visited[x][y] = True
#     if board[x][y] == 1:
#         cnt += 1
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             if visited[nx][ny] == False and board[nx][ny] == 1:
#                 dfs(nx, ny)
#
# cnt = 0
# housing = []
#
# for i in range(n):
#     for j in range(n):
#         if board[i][j] == 1 and visited[i][j] == False:
#             dfs(i,j)
#             housing.append(cnt)
#             cnt = 0
#
# # 문제 답 도출
# housing.sort() # 오름차순 정렬
# print(len(housing))
# for i in housing:
#     print(i)

    # board = int(input())

    # if d == m:
    #     print("~~~~답이 나올 듯")

    # return


    # for i in board:
    #     for j in board:
    #         if board[i][j] == False:
    #             board[i][j] = True
    #             dfs(d+i, n, m)
    #
    #
    #         if board[i][j] == 1 or board[i][j] == 0:
    #             nx = x + dx[i]
    #             ny = y + dy[j]
    #         dfs(d+1,n,m)


n = int(input()) # 테스트 케이스의 개수임
graph = [] # 지도를 받을 배열
num = [] # ??

# 지도의 테스트케이스를 다 넣음
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우를 다 확인하기 위한 코드
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):

    # 마이너스 위치 또는 그 벽의 넘으면 False로 리턴한다
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

# 1이 있으면 옆으로 넘어간다
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0 # 왜 다시 0으로 초기화 해주는거지?
        for i in range(4): # 4가지 방향을 다 둘러보기 위해서 4임
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False


count = 0
result = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])




