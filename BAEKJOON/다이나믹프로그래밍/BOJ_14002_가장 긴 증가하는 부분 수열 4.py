import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):

        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

order = max(dp)
answer = []
for i in range(n - 1, -1, -1):

    if dp[i] == order:
        answer.append(num[i])
        order -= 1

answer.sort()
print(*answer)
