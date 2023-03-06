import sys

input = sys.stdin.readline

n = int(input())

height = []
for _ in range(n):
    a, b = map(int, input().split())
    height.append((a,b))

answer = []
for i in range(n):
    cnt = 0
    for j in range(n):

        if height[i][0] < height[j][0] and height[i][1] < height[j][1]:
            cnt += 1
    answer.append(cnt + 1)

print(answer)