import sys

input = sys.stdin.readline


n = int(input())

answer = []
for _ in range(n):

    board = list(map(int, input().split()))

    board.sort(reverse = True)
    print(board[2])