import sys

input = sys.stdin.readline

'''

1. 홍준이는 미로 안의 한 칸에 남쪽을 보며 서있다.
2. 지도의 크기는 어떻게 정하는데 ?
3. 

동 = (0,1)
서 = (0,-1)
남 = (1,0)
북 = (-1,0) 

'''

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs():

    return

n = int(input())
order = input()

# 바라보는 방향
dire = [0,1,2,3]
x,y,dire = 0,0,1

graph = [[0,0]]
#
# board =
#
# hong =



for i in order:

    if 'R' == i:
        dire = (dire + 1) % 4
    if 'L' == i:
        dire = (dire - 1) % 4
    if 'F' == i:
        x = x + dx[dire]
        y = y + dy[dire]
        graph.append([x,y])

n = max(graph)[0] - min(graph)[0] + 1

m = max(graph, key = lambda x:x[1])[1] - min(graph, key = lambda x:x[1])[1] + 1

min_x = min(graph, key = lambda x:x[0])[0]
min_y = min(graph, key = lambda x:x[1])[1]

for i in graph:
    i[0] = i[0] + abs(min_x)
    i[1] = i[1] + abs(min_y)


map = [[False] * m for _ in range(n)]

for i in graph:
    if map[i[0]][i[1]] == False:
        map[i[0]][i[1]] = '.'

for i in map:
    for j in range(m):
        if i[j] == False:
            i[j] = '#'

for i in map:
    for j in range(len(i)):
        print(i[j], end='')
    print('')


print(graph)