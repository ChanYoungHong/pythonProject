n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):

    return



cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == True:
            cnt += 1

print(cnt)