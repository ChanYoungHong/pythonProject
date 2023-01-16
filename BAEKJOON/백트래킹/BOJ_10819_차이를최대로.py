import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
sum = 0
visited = [False] * (n + 1)
result = 0
answer = []

def dfs(dep):
    global result
    if dep == n:
        sum = 0
        for i in range(n-1):
            sum += abs(answer[i] - answer[i+1])
        result = max(result, sum)

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            answer.append(array[i])
            dfs(dep + 1)
            answer.pop()
            visited[i] = False

dfs(0)
print(result)
