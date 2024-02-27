import sys

input = sys.stdin.readline

t = int(input())

ans = []
for i in range(t):

    a = int(input())

    if a == 0:
        ans.pop()
    else:
        ans.append(a)

print(sum(ans))