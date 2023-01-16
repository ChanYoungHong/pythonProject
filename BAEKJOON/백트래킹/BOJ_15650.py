'''
1. 중복을 제거해야 하는데 그걸 어떻게 하지?
2.
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
result = []
def dfs(start):

    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(start, n+1):
        if i not in result:
            result.append(i)
            dfs(i+1)
            result.pop()

dfs(1)

