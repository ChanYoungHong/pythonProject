import sys

input = sys.stdin.readline
'''
1. 1개 or 3개
2. 상근 sk 상근이 먼저 가져 감
3. 창영 cy

'''
n = int(input())

dp = [-1] * (1001)

dp[1] = 0
dp[2] = 1
dp[3] = 0
dp[4] = 1

for i in range(4, 1001):

    if dp[i-1] == 1 or dp[i-3] == 1:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[n] == 1:
    print('SK')
else:
    print('CY')