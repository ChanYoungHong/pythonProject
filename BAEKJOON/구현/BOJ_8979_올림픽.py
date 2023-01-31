import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
result = []
for i in range(n):

    graph = list(map(int, input().split()))

    if graph[0] != m:
        result.append(graph)
    else:
        standard = graph

cnt = 1
for i in range(len(result)):
    if result[i][1] > standard[1]:
        cnt += 1

    elif result[i][1] == standard[1]:
        if result[i][2] > standard[2]:
            cnt += 1
        elif result[i][2] == standard[2]:
            if result[i][3] > standard[3]:
                cnt += 1


print(cnt)
