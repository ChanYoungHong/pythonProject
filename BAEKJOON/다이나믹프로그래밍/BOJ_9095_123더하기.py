import sys

input = sys.stdin.readline


''' 
점화식 - > dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
'''
def zzz(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return zzz(n-1) + zzz(n-2) + zzz(n-3)

test = int(input())

for _ in range(test):
    te = int(input())
    print(zzz(te))

