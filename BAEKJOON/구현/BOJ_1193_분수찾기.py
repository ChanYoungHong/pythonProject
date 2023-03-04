import sys

input = sys.stdin.readline

n = int(input())

line = 0
''' n이 line보다 더 클 때까지만 반복해라'''
''' 즉, line이 더 클 땐 빠져나감'''
while n > line:
    n -= line
    line += 1

print(n, line)

if line % 2 == 0:
    a = n
    b = line - n + 1
elif line % 2 == 1:
    a = line - n + 1
    b = n

a = str(a)
b = str(b)

print(a+'/'+b)


