import sys

input = sys.stdin.readline


n = int(input())
line = 0

while n > line:
    n -= line
    line += 1

print(n, line)

if line % 2 == 0:
    a = n # 분자가 점점 커질 때
    b = line - n + 1
elif line % 2 == 1:
    a = line - n + 1
    b = n # 분모가 점점 커질 때

print(str(a)+'/'+str(b))