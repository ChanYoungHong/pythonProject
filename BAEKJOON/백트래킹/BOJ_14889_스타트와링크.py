'''
1. 시간복잡도 : 아무구현이나 하면 됨
2. 아이디어 : 최소값을 구하기 위해서 min을 사용해야 할 것 같음


'''

import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

res = sys.maxsize

visit = [False] * n


def dfs(dep, idx):
    global res

    if dep == (n // 2):
        start, link = 0, 0

        for i in range(n): # 0 1 2 3
            for j in range(i + 1, n):

                if visit[i] and visit[j]:
                    start += (graph[i][j] + graph[j][i])
                elif not visit[i] and not visit[j]:
                    link += (graph[i][j] + graph[j][i])

        res = min(res, abs(start - link))

    for i in range(idx, n):
        if not visit[i]:
            visit[i] = True
            dfs(dep + 1, i + 1)
            visit[i] = False


dfs(0, 0)
print(res)
