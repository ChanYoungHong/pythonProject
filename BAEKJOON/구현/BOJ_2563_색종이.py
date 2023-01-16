import sys

input = sys.stdin.readline

n = int(input())
graph = [[0] * 100 for _ in range(100)]

for _ in range(n):
    a, b = map(int, input().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            graph[i][j] = 1


result = 0
for i in graph:
    result += i.count(1)

print(result)

