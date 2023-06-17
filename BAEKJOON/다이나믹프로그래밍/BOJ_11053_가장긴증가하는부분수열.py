import sys

input = sys.stdin.readline

'''
1. 1 < n < 1000 사이에 있으니깐 
2. 이중 for문으로 풀 수 있을 듯

'''

n = int(input())
arr = list(map(int, input().split()))

dp = [1] *n

for i in range(n):
    for j in range(i):

        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# print(dp)
print(max(dp))


