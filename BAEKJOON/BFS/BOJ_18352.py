'''

1. 시간복잡도 - nlongn이 되어야 함
2. 아이디어 - result 배열을 하나 만들어서 길이가 K가 되면 result에 append

'''

import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()

    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)

if k in distance:
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)
else:
    print(-1)