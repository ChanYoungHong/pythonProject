import sys

input = sys.stdin.readline

n, m = map(int, input().split())
result = []


def dfs(dep):

    if len(result) == m:
        print(*result)
        return

    for i in range(dep, n+1):
        if i not in result:
            result.append(i)
            dfs(i + 1)
            result.pop()

dfs(1)
