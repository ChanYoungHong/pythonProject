import sys

input = sys.stdin.readline

n,k,s = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

cnt = 0
total = 0
stand = k*s

for i in range(len(arr)):

    if stand > total:
        total += arr[i]
        cnt += 1

    if stand <= total:
        break

print(cnt)
