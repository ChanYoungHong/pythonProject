import sys
input = sys.stdin.readline

n = int(input())
grape = [0]

for _ in range(n):
    grape.append(int(input().rstrip()))

print(grape)
dp = [0]
dp.append(grape[1])

if n > 1:
    dp.append(grape[1] + grape[2])

for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-3] + grape[i-1] + grape[i], dp[i-2] + grape[i]))

print(dp[n])


''''''
# n = int(input())
# w = [0]
# for i in range(n):
#     w.append(int(input()))
# dp = [0]
# dp.append(w[1])
# if n > 1:
#     dp.append(w[1] + w[2])
# for i in range(3, n + 1):
#     dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i]))
# print(dp[n])

