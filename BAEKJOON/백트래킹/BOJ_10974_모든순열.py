import sys

input = sys.stdin.readline

n = int(input())

res = []
def dfs():

    if len(res) == n:
        print(*res)

    for i in range(1, n+1):
        if i not in res:
            res.append(i)
            dfs()
            res.pop()

dfs()