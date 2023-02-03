import sys

input = sys.stdin.readline

n = int(input())

result = []


def dfs(start):
    if len(result) == n:
        print(*result)
        return

    for i in range(start, n + 1):
        if i not in result:
            result.append(i)
            dfs(i)
            result.pop()


dfs(1)
