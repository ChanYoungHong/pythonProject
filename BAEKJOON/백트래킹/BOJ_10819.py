import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
visited = [False] * n
answer = 0
tem = []

def dfs(d):
    global answer

    if d == n:
        sum = 0
        for i in range(n-1):
            sum += abs(tem[i] - tem[i+1])
        answer = max(sum, answer)
        return

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            tem.append(array[i])
            dfs(d+1)
            visited[i] = False
            tem.pop()

dfs(0)
print(answer)