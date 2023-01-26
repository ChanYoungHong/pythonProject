import sys

input = sys.stdin.readline

n, m = map(int, input().split())

result = []
def dfs():

    if len(result) == m:
        print(*result)
        return

    for j in range(1, n + 1):
        result.append(j)
        dfs()
        result.pop()

dfs()

