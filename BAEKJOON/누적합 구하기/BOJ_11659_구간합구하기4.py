import sys

input = sys.stdin.readline

'''
n < 100000 이니깐 nlogn을 사용해서 이진탐색 방법으로 접근해야 할 듯

'''

n,m = map(int, input().split())
arr = list(map(int, input().split()))

dp = []
dp.append(0)

sum = 0
for i in range(n):
    sum += arr[i]
    dp.append(sum)

# print(dp)


for _ in range(m):
    a,b = map(int, input().split())


    # for k in range(1, n+1):
    ans = dp[b] - dp[a-1]
    print(ans)

# print(dp)
