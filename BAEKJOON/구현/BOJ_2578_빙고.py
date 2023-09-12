import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
mc = []

for i in range(5):
    mc += list(map(int, input().split()))


def check():
    bingo = 0

    # 가로검사
    for i in board:
        if i.count(0) == 5:
            bingo += 1

    # 세로검사
    for k in range(5):
        t = 0
        for z in range(5):
            if board[z][k] == 0:
                t += 1

        if t == 5:
            bingo += 1

    # 왼쪽 대각선 검사
    d1 = 0
    for qq in range(5):
        if board[qq][qq] == 0:
            d1 += 1

    if d1 == 5:
        bingo += 1

    # 오른쪽 대각선 검사
    d2 = 0
    for v in range(5):
        if board[v][4 - v] == 0:
            d2 += 1

    if d2 == 5:
        bingo += 1

    return bingo


cnt = 0
for i in range(25):
    for j in range(5):
        for k in range(5):

            if mc[i] == board[j][k]:
                board[j][k] = 0
                cnt += 1


    if cnt >= 12:
        result = check()

        if result >= 3:
            print(i+1)
            break
