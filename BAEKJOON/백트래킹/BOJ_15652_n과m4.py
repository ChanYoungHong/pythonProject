'''
1. 시간복잡도 -
2. 아이디어 -

'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
result = []


def dfs(dep, idx):
    if len(result) == m:
        print(*result)
        return

    for i in range(idx, n + 1):
        result.append(i)
        dfs(dep, i)
        result.pop()


dfs(1,1)
