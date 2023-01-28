import sys

input = sys.stdin.readline

n, m = map(int, input().split())

res = []


def dfs(dep):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    for i in range(1, n + 1):
        res.append(i)
        dfs(dep + 1)
        res.pop()


dfs(1)
