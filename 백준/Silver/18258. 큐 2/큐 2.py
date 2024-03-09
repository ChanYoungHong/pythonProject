import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

temp = deque([])

for _ in range(n):

    order = input().split()

    if order[0] == 'size':
        print(len(temp))
    elif order[0] == 'front':
        if len(temp) > 0:
            print(temp[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if len(temp) > 0:
            print(temp[-1])
        else:
            print(-1)
    elif order[0] == 'pop':
        if len(temp) > 0:
            print(temp.popleft())
        else:
            print(-1)
    elif order[0] == 'empty':
        if len(temp) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'push':
        temp.append(order[1])