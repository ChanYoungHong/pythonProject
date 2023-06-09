import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):

    stick, ant = map(int, input().split())

    max_stick = []
    min_stick = []

    for j in range(ant):

        loc = int(input())

        loc = min(loc, stick - loc)
        min_stick.append(loc)

        loc = max(loc, stick - loc)
        max_stick.append(loc)

    print(max(min_stick), max(max_stick))