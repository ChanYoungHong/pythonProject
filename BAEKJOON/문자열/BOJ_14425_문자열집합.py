import sys

input = sys.stdin.readline

n, m = map(int, input().split())


a = []
for _ in range(n):
    a.add(input().rstrip())

cnt = 0
for j in range(m):

    t = input().rstrip()

    if t in a:
        cnt += 1

print(cnt)

# b = set()
# for _ in range(m):
#     b.add(input().rstrip())
#
# for j in a:
#     if j in b:
#         res.append(j)
#
#
# print(len(res))