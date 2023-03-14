import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

visited = [False] * (n+1)

graph = [[] for _ in range(n+1)]

for i in range(m):

    a,b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

def bfs(start):

    q = deque([start])
    # graph[start] 을 사용하게 되면 연결된 수 2,5가 들어 감
    # q = deque(graph[start])
    # q.append(start)

    print('q = ', q)
    cnt = 0
    while q:

        t = q.popleft()
        visited[t] = True

        for i in graph[t]:

            if visited[i] == False:
                visited[i] = True
                q.append(i)
                cnt += 1

    print(cnt)

bfs(1)
