import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())


if a == b == c:
    print('Equilateral')
elif (a+b+c) == 180:
    if a == b or b == c or a == c:
        print('Isosceles')
    elif a != b or b != c or a != c:
        print('Scalene')
elif (a+b+c) != 180:
    print('Error')