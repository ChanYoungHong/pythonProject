import sys

input = sys.stdin.readline

n = int(input())

cnt = 0
inter_num = 0
end = 0

for start in range(n):

    while inter_num < n and end < n:
        inter_num += end + 1
        end += 1

    if inter_num == n:
        cnt += 1

    inter_num -= start+1

print(cnt)
