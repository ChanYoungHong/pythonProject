import sys
input = sys.stdin.readline


'''
<포인트>

1. 새로운 칸의 알파벳은 지나온 칸의 알파벳과 달라야 함
2. 


'''

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y, word):

    global answer, cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] not in word:
                dfs(nx, ny, word + board[nx][ny])


    answer = max(answer, len(word))


n,m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

cnt = 0
answer = 0


dfs(0,0,board[0][0])
print(answer)


