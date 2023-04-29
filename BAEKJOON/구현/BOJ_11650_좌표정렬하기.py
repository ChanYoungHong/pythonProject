import sys

input = sys.stdin.readline

n = int(input().rstrip())
res = []

for _ in range(n):
    a,b = map(int, input().rstrip().split())
    res.append((a,b))

res = sorted(res, key=lambda x:(x[0], x[1]))

for i in res:
    print(i[0], i[1])

