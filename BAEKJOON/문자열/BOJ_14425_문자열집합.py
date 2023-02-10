import sys

input = sys.stdin.readline

n, m = map(int, input().split())

s = []

# for i in range(n):
#     s.append(input().rstrip())
#
#
# res = []
# ans = []
# for j in range(m):
#
#     res.append(input().rstrip())
#
#     if res[j] in s:
#         ans.append(res[j])
#
# print(len(ans))

for i in range(n):
    s.append(input().rstrip())

cnt = 0
for j in range(m):

    t = input().rstrip()

    if t in s:
        cnt += 1

print(cnt)

