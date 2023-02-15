import sys

input = sys.stdin.readline

n, m = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

for i in range(n-1):

    if oven[i] < oven[i+1]:
        oven[i+1] = oven[i]


dep = 0

for j in range(n-1, 0, -1):

    if oven[j] >= pizza[dep]:
        dep += 1

    if dep >= m:
        print(j+1)
        sys.exit()

print(0)

