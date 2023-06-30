import sys

input = sys.stdin.readline

'''

브루스 포트로 다 넣어서 
조건에 맞으면 답을 도출하면 될 듯

무슨 사탕을 기준으로 최대를 구하나 ?? 

- 부르프 포스를 사용
- 가장 긴 연속 부분 행 or 열을 고른 다음에 사탕을 모두 먹는다.
- 사탕이 채워진 상태에서 상근이가 먹을 수 있는 사탕의 최대 개수는 ?

푸는 방향 인접한 모든 사탕을 다 뒤짚어보고 
먹을 수 있는 최대 개수를 구하는 방향으로 풀기
'''


n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
maxCnt = 0

def count_candy():
    global maxCnt

    # 행 검사
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
                maxCnt = max(cnt, maxCnt)
            else:
                cnt = 1

        # 열 검사
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
                maxCnt = max(cnt, maxCnt)
            else:
                cnt = 1



for i in range(n):
    for j in range(n):

        # 오른쪽과 바꿈
        if j + 1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            count_candy()
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        # 아래쪽과 바꿈
        if i + 1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            count_candy()
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(maxCnt)













