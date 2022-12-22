n = int(input())
graph = [[0] * 100 for _ in range(100)]

cnt = 0
for _ in range(n):
    a, b = map(int, input().split())

    for i in range(a, a + 10):
        for j in range(b, b + 10):
            graph[i][j] = 1

for z in graph:
    cnt += z.count(1)

print(cnt)
