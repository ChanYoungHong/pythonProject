'''

1. 시간복잡도 -
2. 아이디어 -

'''


import sys

input = sys.stdin.readline

n = int(input())
def sol(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n-1) + sol(n-2) + sol(n-3)

for i in range(n):
    z = int(input())
    print(sol(z))


# for _ in range(n):
#     z = int(input())
#
#     for i in range(3, z+1):
#         dp[i] = dp[z-1] + dp[z-2] + dp[z-3]
#         print(dp[z])