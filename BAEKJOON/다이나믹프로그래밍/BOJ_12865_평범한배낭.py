import sys

input = sys.stdin.readline

n, m = map(int, input().split())

stuff = [[0,0]]
for _ in range(n):
    stuff.append(list(map(int, input().split())))


knapsack = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):

        w = stuff[i][0]
        v = stuff[i][1]

        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(v + knapsack[i-1][j-w], knapsack[i-1][j])

print(knapsack[n][m])