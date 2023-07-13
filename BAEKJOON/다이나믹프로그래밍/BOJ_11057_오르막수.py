import sys

input = sys.stdin.readline
'''
1. 알고리즘 - 
2. 시간복잡도 - 1000 사이라 dp 사용하면 충분
3. 배열? 뭐 키워드 - 

'''
n = int(input())
dp = [1] * 10

for i in range(1, n):
    for j in range(1, 10):
        dp[j] += dp[j-1]

print(sum(dp)%10007)
