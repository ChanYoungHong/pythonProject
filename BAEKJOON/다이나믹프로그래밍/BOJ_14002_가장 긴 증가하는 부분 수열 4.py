import sys

input = sys.stdin.readline

'''
1. 1 < n < 1000 사이에 있음 - 시간 복잡도 고려하기 

'''

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):

        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

# print(dp)

order = max(dp)
res = []

for j in range(n-1, -1, -1):

    # print('j : ', j, end=' ')
    if order == dp[j]:
        res.append(arr[j])
        order -= 1

print(len(res))
res.sort()
print(*res)