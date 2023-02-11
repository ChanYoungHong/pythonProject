import sys

input = sys.stdin.readline


n = int(input())
s = []

while n > 0:
    temp = n % 2
    s.append(temp)
    n = n // 2

ans = 0
for i in range(len(s)):
    if s[i] == 1:
        ans += 3 ** i

print(ans)
