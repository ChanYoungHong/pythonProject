import sys

input = sys.stdin.readline
INF = sys.maxsize

alph = 'abcdefghijklnmopqrstuvwxyz'
t = len(alph)

graph = [[INF] * t for _ in range(t)]

n = int(input())
for i in range(n):
    a,b = map(alph.index, input().rstrip().split(" is "))
    graph[a][b] = 1


for k in range(t):
    for i in range(t):
        for j in range(t):

            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

m = int(input())
for j in range(m):
    a, b = map(alph.index, input().rstrip().split(" is "))

    if graph[a][b] == 'INF':
        print('F')
    else:
        print('T')