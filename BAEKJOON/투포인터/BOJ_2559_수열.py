import sys

input = sys.stdin.readline

n,k = map(int, input().split())
arr = list(map(int, input().split()))
each = sum(arr[:k])

maxv = each

for i in range(k, n):
    each += arr[i]
    each -= arr[i-k]
    maxv = max(maxv, each)

print(maxv)