import sys

input = sys.stdin.readline

n = int(input())
mapp = []

for _ in range(n):
    mapp.append(list(map(int, input().split())))

visit = [False] * n



result = 1e9
def dfs(dep, idx):
    global result

    if dep == (n // 2):
        start, link = 0, 0
        for i in range(n):
            for j in range(i + 1, n):
                if visit[i] and visit[j]:
                    start += (mapp[i][j] + mapp[j][i])
                elif not visit[i] and not visit[j]:
                    link += (mapp[i][j] + mapp[j][i])
        result = min(result, abs(start - link))

    for i in range(idx, n):
        if not visit[i]:
            visit[i] = True
            dfs(dep + 1, i + 1)
            visit[i] = False


dfs(0, 0)
print(result)