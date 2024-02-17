import sys

input = sys.stdin.readline

n = int(input())


def gcb(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcb(a, b):
    tem = (a * b) // gcb(a, b)
    return tem


for _ in range(n):
    a, b = map(int, input().rstrip().split())
    # print('gcb : ', gcb(a, b))
    print(lcb(a, b))