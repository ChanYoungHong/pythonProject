import sys

input = sys.stdin.readline

dp = [0 for i in range(101)]

dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(0, 98):
    dp[i+3] = dp[i] + dp[i+1]

t = int(input())
for i in range(t):
    n = int(input())
    print(dp[n])

'''

1 2 3 4 5 6 7 8 9 10 11
1 1 1 2 2 3 4 5 7 9 12

idx 1 + 3 -> 4
값   1 + 1 -> 2

idx 3 + 5 -> 6
값   1 + 2 -> 3

idx 2 + 6 -> 7
값   1 + 3 -> 4 

idx 1 + 7 -> 8
값   1 + 4 -> 5


'''
