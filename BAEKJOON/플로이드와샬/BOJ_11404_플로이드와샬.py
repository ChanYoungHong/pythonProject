'''

'''

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = sys.maxsize

s = [[INF] * (n + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            s[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    s[a][b] = min(s[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            s[i][j] = min(s[i][j], (s[i][k] + s[k][j]))

for i in range(1, n+1):
    for j in range(1, n+1):
        if s[i][j] == INF:
            print(0, end=' ')
        else:
            print(s[i][j], end=' ')
    print()
