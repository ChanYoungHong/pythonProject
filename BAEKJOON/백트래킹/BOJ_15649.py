import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
visited = [False] * (n + 1)
result = []


def dfs(dep):
    if dep == m:
        print(' '.join(map(str, result)))
        return

    for i in range(1, n + 1):
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            dfs(dep+1)
            visited[i] = False
            result.pop()

dfs(0)
