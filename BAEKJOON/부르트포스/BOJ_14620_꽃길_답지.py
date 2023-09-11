import sys
from collections import deque

input = sys.stdin.readline

'''
1. 꽃 씨앗이 3개, 닿게 될 경우 두 꽃이 죽어버림
2. dfs, bfs 중에 뭘로 사용해야 될까? 
3. 꽃이 필려면 주변에 피었는지 확인을 해야하지 않을까? - 겹치면 죽기 때문에
4. 

'''

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 주변의 4개의 방향을 확인하기 !
def check(x, y, visited):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (nx, ny) in visited:
            return False
    return True


def dfs(visited, total):
    global answer

    if total >= answer:
        return

    if len(visited) == 15:
        answer = min(total, answer)

    else:

        # 가장 자리에는 꽃을 심을 수 없기 때무네 1, n-1로 범위를 설정한다.
        for i in range(1, n - 1):
            for j in range(1, n - 1):

                if check(i, j, visited) and (i, j) not in visited:

                    temp = [(i, j)]
                    temp_cost = board[i][j]

                    for q in range(4):
                        nx = i + dx[q]
                        ny = j + dy[q]
                        temp.append((nx, ny))
                        temp_cost += board[nx][ny]

                        print('visited : ', visited)
                        print('temp : ', temp)
                        print(' ++ ', visited + temp)
                    dfs(visited + temp, total + temp_cost)


n = int(input())
answer = 1e9

board = [list(map(int, input().split())) for _ in range(n)]
dfs([], 0)
print(answer)
