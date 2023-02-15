'''

-> 왜 bfs를 사용해야 하는지 ??
-> 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하라 !??
->

아이디어 : 사실 문제가 잘 이해가 되지 않는다..


'''

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maps = [[] for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append([b, c])
    maps[b].append([a, c])

start, end = map(int, input().split())
low, high = 1, 1000000000


def bfs(mid):

    q = deque()
    q.append(start)
    visited[start] = True

    while q:

        now = q.popleft()
        if now == end:
            return True

        for node, cost in maps[now]:
            if not visited[node] and mid <= cost:
                q.append(node)
                visited[node] = True

    return False


ans = 0
while low <= high:

    mid = (low + high) // 2
    visited = [False for _ in range(n + 1)]

    if bfs(mid):
        ans = max(ans, mid)
        low = mid + 1

    else:
        high = mid - 1

print(ans)