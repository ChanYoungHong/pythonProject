import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

a = set()

for i in range(n):
    a.add(input().rstrip())

b = set()
for i in range(m):
    b.add(input().rstrip())

same = sorted(set(a&b))

print(len(same))
for i in same:
    print(i)