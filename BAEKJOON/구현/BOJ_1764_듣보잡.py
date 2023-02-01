
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

a = set()
for i in range(n):
    a.add(input().rstrip())

b = set()
for i in range(m):
    b.add(input().rstrip())

result = sorted(list(a & b))

print(len(result))
for i in result:
    print(i)

# no_lis = []
# no_see = []
# z = n + m
#
# for i in range(z):
#
#     names = input().rstrip()
#     no_lis.append(names)
#
#     if no_lis.count(no_lis[i]) >= 2:
#         no_see.append(no_lis[i])
#
# print(len(no_see))
# for i in no_see:
#     print(i)

