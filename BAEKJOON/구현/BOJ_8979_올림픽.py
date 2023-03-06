import sys

input = sys.stdin.readline

n, m = map(int, input().split())

tempArr = []
for i in range(n):

    graph = list(map(int, input().split()))

    if graph[0] != m:
        tempArr.append(graph)
    else:
        standard = graph

cnt = 1
for i in range(len(tempArr)):

    if tempArr[i][1] > standard[1]:
        cnt += 1
    elif tempArr[i][1] == standard[1]:
        if tempArr[i][2] > standard[2]:
            cnt += 1
        elif tempArr[i][2] == standard[2]:
            if tempArr[i][3] > standard[3]:
                cnt += 1

print(cnt)

