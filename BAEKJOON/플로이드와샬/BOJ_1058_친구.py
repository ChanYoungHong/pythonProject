import sys

input = sys.stdin.readline

N = int(input())
graph = [list(input().rstrip())for _ in range(N)]

visited = [[0] * N for _ in range(N)]
res = []
cnt = 0

# 플로이드 와샬 알고리즘
for k in range(N):  # 경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(N):
        for j in range(N):

            if i == j:
                continue
            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
                visited[i][j] = 1

result = 0


print(result)
print(visited)
print(graph)
print(sum(visited))
