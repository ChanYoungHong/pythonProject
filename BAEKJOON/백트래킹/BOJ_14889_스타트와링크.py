'''
1. 시간복잡도 : 아무구현이나 하면 됨
2. 아이디어 : 최소값을 구하기 위해서 min을 사용해야 할 것 같음


'''

import sys

input = sys.stdin.readline

n = int(input())
result = sys.maxsize
# graph = list(map(int, input().split()))
array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# visited = [[False] * (n) for _ in range(n)]

visited = [False] * (n+1)
result = 0
def dfs(dep, idx):
    global result

    if dep == (n//2):
        start, link = 0,0

        for i in range(n):
            for j in range(i+1, n):

                if visited[i] and visited[j]:
                    start += (array[i][j] + array[j][i])
                elif not visited[i] and not visited[j]:
                    link += (array[i][j] + array[j][i])
        result = min(result, abs(start - link))

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(dep + 1, i + 1)
            visited[i] = False

dfs(0, 0)
print(result)
