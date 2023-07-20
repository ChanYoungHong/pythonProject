import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ssum = 0
res = [0]
for k in range(n):
    ssum += arr[k]
    res.append(ssum)

m = int(input())
for i in range(m):
    x,y = map(int, input().split())
    print(res[y] - res[x-1])





