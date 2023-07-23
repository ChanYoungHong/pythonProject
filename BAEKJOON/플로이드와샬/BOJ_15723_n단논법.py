import sys

input = sys.stdin.readline
INF = sys.maxsize

alph = 'abcdefghijklnmopqrstuvwxyz'

t = len(alph)

board = [[INF] * t for _ in range(t)]

n = int(input())
for i in range(n):
    a,b = map(alph.index, input().rstrip().split(" is "))
    board[a][b] = 1

for k in range(t):
    for i in range(t):
        for j in range(t):

            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

m = int(input())
for j in range(m):
    a,b = map(alph.index, input().rstrip().split(" is "))

    if board[a][b] == INF:
        print('F')
    else:
        print('T')

