import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a,b = input().rstrip().split()
    ans = ''
    for i in b:
        ans += int(a)*i

    print(ans)
