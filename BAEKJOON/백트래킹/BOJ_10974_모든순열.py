import sys

input = sys.stdin.readline

n = int(input())
result = []

def dfs(dep):

    if dep == n:
        print(*result)
        return

    for i in range(1, n+1):
        if i not in result:
            result.append(i)
            dfs(dep+1)
            result.pop()

dfs(0)