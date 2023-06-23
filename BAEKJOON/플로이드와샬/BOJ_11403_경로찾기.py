import sys

input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):

            # if i == j:
            #     continue

            if s[i][j] == 1 or (s[i][k] == 1 and s[k][j] == 1):
                s[i][j] = 1

for i in s:
    print(*i, end=' ')
    print()

