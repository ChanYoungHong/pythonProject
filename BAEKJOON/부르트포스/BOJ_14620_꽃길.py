import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9


dx = [1,-1,0,0]
dy = [0,0,1,-1]
def check(x,y,visited):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (nx,ny) in visited:
            return False
    return True

def dfs(visited, total):

    global answer

    if total >= answer:
        return

    if len(visited) == 15:
        answer = min(total, answer)

    else:

        for i in range(1, n-1):
            for j in range(1, n-1):

                if check(i,j,visited) and (i,j) not in visited:

                    temp = [(i,j)]
                    temp_cost = board[i][j]

                    for ww in range(4):
                        nx = i + dx[ww]
                        ny = j + dy[ww]
                        temp.append((nx,ny))
                        temp_cost += board[nx][ny]
                    dfs(visited + temp, temp_cost + total)

dfs([], 0)
print(answer)