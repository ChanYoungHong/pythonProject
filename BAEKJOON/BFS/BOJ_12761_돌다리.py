import sys
from collections import deque

input = sys.stdin.readline


a,b,n,m = map(int, input().split())

d = [1, -1, a, -a, b, -b, a, b]
arr = [0 for i in range(100001)]
visited = [0 for i in range(100001)]
visited[n] = 1


def bfs():

    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        for i in range(8):
            if i < 6:
                nx = x + d[i]
                if 0 <= nx <= 100000 and not visited[nx]:
                    q.append(nx)
                    visited[nx] = 1
                    arr[nx] = arr[x] + 1
            else:
                nx = x * d[i]
                if 0 <= nx <= 100000 and not visited[nx]:
                    q.append(nx)
                    visited[nx] = 1
                    arr[nx] = arr[x] + 1


bfs()
print(arr[m])








