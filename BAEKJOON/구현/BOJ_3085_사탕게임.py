import sys

input = sys.stdin.readline

'''

브루스 포트로 다 넣어서 
조건에 맞으면 답을 도출하면 될 듯

무슨 사탕을 기준으로 최대를 구하나 ?? 

'''




def count_candy():
    row_cnt, col_cnt, row_max, col_max = 1, 1, -1e9, -1e9

    # 행을 check 한다.
    for i in range(n):
        for j in range(n - 1):

            if board[i][j] == board[i][j + 1]:
                row_cnt += 1
            else:
                row_cnt = 1
            row_max = max(row_cnt, row_max)
        row_cnt = 1

    # 열을 check 한다.
    for j in range(n):
        for i in range(n - 1):

            if board[i][j] == board[i + 1][j]:
                col_cnt += 1
            else:
                col_cnt = 1
            col_max = max(col_cnt, col_max)
        col_cnt = 1
    answer = max(row_max, col_max)

    return answer

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ans = 0

for i in range(n):
    for j in range(n):

        # 0 1 2 3
        for k in range(4):
            nx = i + steps[k][0]
            ny = j + steps[k][1]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if board[i][j] != board[nx][ny]:
                board[nx][ny], board[i][j] = board[i][j], board[nx][ny]
                ans = max(ans, count_candy())
                # 다시 재자리로 돌려준다 왜 ?
                board[i][j], board[nx][ny] = board[nx][ny], board[i][j]

print(ans)
