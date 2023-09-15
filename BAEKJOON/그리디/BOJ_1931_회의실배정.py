import sys

input = sys.stdin.readline

n = int(input())

res = []
for _ in range(n):
    a, b = map(int, input().split())
    res.append((a, b))

res = sorted(res, key=lambda x: x[0])
res = sorted(res, key=lambda x: x[1])

# print(res)

last = 0
cnt = 0
for i, j in res:

    if i >= last:
        last = j
        cnt += 1

print(cnt)

#
#     # last = j
#     #
#     # if last > i:
#     #     continue
#     # else:
#     #     last = j
#     #     cnt += 1
#
# print(cnt)
