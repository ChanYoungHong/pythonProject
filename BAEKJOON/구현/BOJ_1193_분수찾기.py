import sys

input = sys.stdin.readline

n = int(input())

line = 0

while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    a = n
    b = line - n + 1

if line % 2 != 0:
    a = line - n + 1
    b = n

a = str(a)
b = str(b)

print(a+'/'+b)
