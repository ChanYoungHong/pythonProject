import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))


cnt = 0
inter_num = 0
end = 0

for i in range(n):

    while inter_num < m and end < n:
        inter_num += arr[end]
        end += 1

    if inter_num == m:
        cnt += 1

    inter_num -= arr[i]

print(cnt)
