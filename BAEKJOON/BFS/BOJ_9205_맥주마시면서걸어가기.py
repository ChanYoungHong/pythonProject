import sys
from collections import deque

input = sys.stdin.readline

'''

1. 맥주 한 박스에 20개 들음
2. 50미터에 한 병씩
3. 빈 병 버리고, 새 맥주 삼
4. 20병을 넘을 수 없음
5. 맥주 1병당 50미터 움직인다.

'''


def bfs():
    q = deque()
    q.append((h_x, h_y))

    while q:

        x,y = q.popleft()

        if abs(x-f_x) + abs(y-f_y) <= 1000:
            print('happy')
            return

        for i in range(n):
            if not visited[i]:
                new_x, new_y = graph[i]

                if abs(x-new_x) + abs(y-new_y) <= 1000:
                    visited[i] = 1
                    q.append((new_x, new_y))

    print('sad')
    return

t = int(input())

for _ in range(t):
    n = int(input())
    h_x, h_y = map(int, input().split())
    graph = []
    for _ in range(n):
        a, b = map(int, input().split())
        graph.append((a, b))
    f_x, f_y = map(int, input().split())
    visited = [0 for _ in range(n + 1)]
    bfs()
