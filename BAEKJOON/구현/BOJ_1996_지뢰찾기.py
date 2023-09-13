import sys

input = sys.stdin.readline


'''
1. 점은 -> 지뢰가 없는 것, 숫자는 지뢰가 있는 경우이다.
2. 숫자 -> 숫자는 지뢰가 있는 경우로 그 칸의 지뢰의 개수이다.
3.
4.
5.

'''

# check = ['1','2','3','4','5','6','7','8','9']
#
# n = int(input())
# board = [list(input().rstrip()) for _ in range(n)]
#
#
# for i in range(n):
#     for j in range(n):
#
#         if board[i][j] in check:
#             board[i][j] = '*'
#
# print(board)

n = int(input())

def init():
    for i in range(n):
        row = input()
        for j in range(n):
            if row[j] != '.':
                mine_pos.append((i,j, int(row[j])))
                b[i].append('*')
            else:
                b[i].append(0)

def set_mine():
    for i,j,c in mine_pos:
        for a in range(8):
            ni, nj = i + di[a], j + dj[a]
            if 0 <= ni < n and 0 <= nj < n and b[ni][nj] != '*':
                if b[ni][nj] != 'M':
                    b[ni][nj] += c
                    if b[ni][nj] >= 10:
                        b[ni][nj] = 'M'

b = [[] for _ in range(n)]
mine_pos = []
di = [-1,-1,-1,0,1,1,1,0]
dj = [-1,0,1,1,1,0,-1,-1]
init()
set_mine()
for e in b:
    print(*e, sep='')