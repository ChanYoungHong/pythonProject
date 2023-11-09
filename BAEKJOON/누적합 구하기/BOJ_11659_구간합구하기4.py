import sys

input = sys.stdin.readline

'''
1. 시간복잡도 - n < 100,000 아래일 때 - 투 포인터, 이진탐색, 부분합 공식 등등 사용
2. 
'''

n,m = map(int, input().split())
arr = list(map(int, input().split()))

summ = 0
dp = []
dp.append(0)
for i in range(n):
    summ += arr[i]
    dp.append(summ)

# print(dp)
for _ in range(m):
    a,b = map(int, input().split())
    print(dp[b] - dp[a-1])