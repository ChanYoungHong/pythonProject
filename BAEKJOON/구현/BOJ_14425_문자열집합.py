import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s = [input() for _ in range(n)]

cnt = 0

for i in range(m):
    t = input()

    if t in s:
        cnt += 1
print(cnt)