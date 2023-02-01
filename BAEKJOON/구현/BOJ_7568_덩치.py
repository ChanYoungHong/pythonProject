import sys

input = sys.stdin.readline

n = int(input())

result = []
for _ in range(n):
    a,b = map(int, input().split())
    result.append((a,b))

answer = []
for i in range(n):
    cnt = 0
    for j in range(n):
        if result[i][0] < result[j][0] and result[i][1] < result[j][1]:
            cnt += 1
    answer.append(cnt+1)

print(*answer)
