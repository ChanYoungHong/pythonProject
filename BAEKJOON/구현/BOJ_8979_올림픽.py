import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

graph = []

cnt = 1
standard = []
for i in range(n):
    z = list(map(int, input().rstrip().split()))

    if z[0] != m:
        graph.append(z)
    else:
        standard = z

for j in range(len(graph)):

    if graph[j][1] > standard[1]:
        cnt += 1
    elif graph[j][1] == standard[1]:
        if graph[j][2] > standard[2]:
            cnt += 1
        elif graph[j][2] == standard[2]:
            if graph[j][3] > standard[3]:
                cnt += 1

print(cnt)
