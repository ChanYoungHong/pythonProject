import sys

input = sys.stdin.readline

t = int(input())

'''

1. 생각해봐야 할 점 -> 

'''

for i in range(t):

    stick, ant = map(int, input().split())

    min_s = []
    max_s = []

    for j in range(ant):

        loc = int(input())

        loc = min(loc, stick - loc)
        min_s.append(loc)

        loc = max(loc, stick - loc)
        max_s.append(loc)

    print(max(min_s), max(max_s))






