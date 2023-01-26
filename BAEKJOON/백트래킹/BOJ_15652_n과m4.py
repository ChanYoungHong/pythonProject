'''
1. 시간복잡도 -
2. 아이디어 -

'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
result = []


def dfs(dep):
    if len(result) == m:
        print(*result)
        return

    for i in range(dep, n+1):
        result.append(i)
        dfs(i)
        result.pop()


dfs(1)
