import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

'''

빈 공간은 -> .(점)
울타리 -> #으로
늑대를 -> v
양 -> k

수도코드 -> 한 영역 안에서 양과 늑대의 개수를 비교한다.

각 영역을 돌 때마다 양 수와 늑대수를 비교한다
if 절로 
만약 양이 많으면 양수 만큼 올려주고
같거나 작으면 늑대를 다 넣어준다.


'''

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]



def dfs(x,y):

    global wolf, sheep
    visited[x][y] = 1


    if board[x][y] == 'v':
        wolf += 1

    if board[x][y] == 'k':
        sheep += 1

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == False and board[nx][ny] != '#':
                dfs(nx,ny)


ans1 = 0
ans2 = 0

wolf, sheep = 0,0

for i in range(n):
    for j in range(m):

        if board[i][j] != '#' and visited[i][j] == False:

            dfs(i,j)

            if wolf >= sheep:
                sheep = 0
            else:
                wolf = 0

            ans1 += sheep
            ans2 += wolf

            sheep = 0
            wolf = 0

print(ans1, ans2)





