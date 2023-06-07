import sys

input = sys.stdin.readline

t = int(input())

s = {}

for i in range(t):
    a, b = input().split()

    if b == 'enter':
        s[a] = b
    else:
        del s[a]

s = sorted(s.keys(), reverse=True)

for j in s:
    print(j)

# ans = Counter(s)
#
# print(s)
# print(ans)
