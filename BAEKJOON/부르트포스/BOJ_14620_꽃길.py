import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check(x, y, visited):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 방문을 했으면 false를 반환한다.
        if (nx, ny) in visited:
            return False
    return True


def dfs(visited, total):

    global answer

    # 무슨 조건이 있었음 - 최소비용으로 구하기 위한 조건인 듯
    if total >= answer:
        return

    # 꽃 3개 즉 15개의 지점이 다 심겼으면 종료하기
    # dfs를 계속 돌리면서 최소비용을 구하기
    if len(visited) == 15:
        answer = min(total, answer)

    else:

        for i in range(1, n-1):
            for j in range(1, n-1):

                # 주변에 좌표가 없는 지 확인한다.
                if check(i,j,visited) and (i,j) not in visited:
                    temp = [(i,j)]
                    temp_cost = board[i][j]

                    for kk in range(4):
                        nx = i + dx[kk]
                        ny = j + dy[kk]
                        temp.append((nx,ny))
                        temp_cost += board[nx][ny]

                    dfs(visited + temp, total + temp_cost)

n = int(input())
answer = 1e9
board = [list(map(int, input().split())) for _ in range(n)]
dfs([], 0)
print(answer)

