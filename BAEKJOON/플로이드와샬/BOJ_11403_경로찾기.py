import sys

input = sys.stdin.readline

'''
1. 아이디어 - 문제에서 '모든 정점'이 포인트가 될 것 같다
2. 시간복잡도 - 플로이드 와샬 쓰면 가능할 듯, 100 미만
3. 자료구조 - 

'''

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

print(board)
for k in range(n):
    for i in range(n):
        for j in range(n):

            if board[i][j] == 1 or (board[i][k] == 1 and board[k][j] == 1):
                board[i][j] = 1

for i in board:
    print(*i, end=' ')
    print()