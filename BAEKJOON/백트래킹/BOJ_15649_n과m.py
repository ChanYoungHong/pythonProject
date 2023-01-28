import sys

input = sys.stdin.readline

n, m = map(int,input().split())

result = []
visited = [False] * (n+1)
def dfs(dep):

    if dep == m:
        print(*result)
        print(' '.join(map(str, result))) # 이 것을 사용하면 더 빠름
        return

    for i in range(1, n+1):
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            dfs(dep+1)
            visited[i] = False
            result.pop()

dfs(0)