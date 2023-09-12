import sys
from collections import deque

input = sys.stdin.readline

'''
1. 시간복잡도
2. 어떻게 bfs로 풀 수 있을까?
3. 가로 선 상의 기준으로 bfs를 돌리나 ?? (00) (01) (02) (03) 이런 식으로 ?
4. 하나의 노드가 얼마나 깊이까지 가는지 모두 확인해서 최단시간을 찾으려면 다 탐색해야하니
bfs가 dfs보다 적합하다고 판다
5. 
'''


# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
#
#

def bfs():

    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)


MAX = 10 ** 5
n, k = map(int, input().split())
dist = [0] * (MAX + 1)

bfs()
