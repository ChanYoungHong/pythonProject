n = int(input())
array = []
result = 1e9
visited = [False] * (n + 1)

for _ in range(n):
    array.append(list(map(int, input().split())))

def dfs(depth, idx):

    global result

    if depth == (n//2):
        start, link = 0,0
        for i in range(n):
            for j in range(i+1, n):
                if visited[i] and visited[j]:
                    start += (array[i][j] + array[j][i])
                elif not visited[i] and not visited[j]:
                    link += (array[i][j] + array[j][i])

        result = min(result, abs(start - link))

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, idx + 1)
            visited[i] = False

dfs(0, 0)
print(result)

