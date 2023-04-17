import sys

input = sys.stdin.readline


def dfs(x):
    visited[x] = True
    num = arr[x]

    if not visited[num]:
        dfs(num)


n = int(input())

for _ in range(n):

    leng = int(input().rstrip())
    arr = [0] + list(map(int, input().rstrip().split()))
    visited = [True] + [False] * leng
    res = 0

    for j in range(1, leng + 1):

        if not visited[j]:
            dfs(j)
            res += 1

    print(res)
