
import sys

input = sys.stdin.readline

n, m = map(int,input().split())
result = []
visited = [False] * (n)
def dfs(dep):

    if dep == m:
        print(*result)
        return

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            result.append(i+1)
            dfs(dep+1)
            visited[i] = False
            result.pop()

dfs(0)