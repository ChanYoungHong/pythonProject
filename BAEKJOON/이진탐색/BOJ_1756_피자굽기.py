import sys

input = sys.stdin.readline

n,m = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))


for i in range(n-1):

    if oven[i] < oven[i+1]:
        oven[i+1] = oven[i]

dep = 0
for i in range(n-1, -1,-1):

    if oven[i] < pizza[dep]:
        continue

    if oven[i] >= pizza[dep]:
        dep += 1

    if dep == m:
        print(i+1)
        sys.exit()

print(0)

