import sys

input = sys.stdin.readline

n = int(input())

array = []
visited = [False] * n

for _ in range(n):
    array.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []
cnt = 0


def dfs(x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if array[x][y] == 1:
        array[x][y] = 0
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


temp = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result.append(cnt)
            temp += 1
            cnt = 0

result.sort()

dfs(0, 0)
print(temp)
for i in result:
    print(i)
