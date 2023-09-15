import sys
from collections import deque

input = sys.stdin.readline


'''

1. 자신의 친구와 
2. 친구의 친구를 초대하기로 했다.

'''

n = int(input())
m = int(input())

graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):

    q = deque()
    visited[v] = 1
    q.append(v)

    while q:

        x = q.popleft()

        for i in graph[x]:

            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[x] + 1

        print(visited)

bfs(1)
result = 0

'자신은 노드 1, 친구의 친구가 2부터 시직이 됨'
for i in range(2, n+1):

    '친구의 친구 이니깐 3까지 그냥 친구면 2'
    if visited[i] < 4 and visited[i] != 0:
        result += 1

print(result)
print(visited)


