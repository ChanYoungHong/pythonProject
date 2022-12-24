n, m = map(int, input().split())

array = []

for _ in range(n):
    array.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):

    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if array[x][y] == 0:
        array[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1

print(cnt)
