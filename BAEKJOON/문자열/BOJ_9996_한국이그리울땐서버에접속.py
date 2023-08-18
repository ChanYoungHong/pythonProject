import sys

input = sys.stdin.readline

n = int(input())
a, b = input().split('*')

for _ in range(n):

    word = input()

    if len(word) < len(a) + len(b):
        print('NE')
    elif word[:len(a)] == a and word[-len(b):] == b:
        print('DA')
    else:
        print('NE')
