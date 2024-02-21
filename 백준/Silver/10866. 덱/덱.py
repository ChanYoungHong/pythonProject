import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

list = deque([])

for _ in range(n):

    order = input().rstrip().split()

    if order[0] == 'push_back':
        list.append(order[1])

    elif order[0] == 'push_front':
        list.appendleft(order[1])

    elif order[0] == 'front':

        if list:
            print(list[0])
        else:
            print(-1)

    elif order[0] == 'back':

        if list:
            print(list[-1])
        else:
            print(-1)

    elif order[0] == 'size':
        print(len(list))

    elif order[0] == 'empty':
        if list:
            print(0)
        else:
            print(1)
    elif order[0] == 'pop_front':

        if list:
            print(list.popleft())
        else:
            print(-1)

    elif order[0] == 'pop_back':

        if list:
            print(list.pop())
        else:
            print(-1)

    # order, num = input().split()

    # if order == 'push_back':
    #     list.append(int(num))
    #     print(list)
    # elif order == 'push_front':
    #     list.appendleft(int(num))
    #     print(list)
    #
    # elif order == 'front':
    #     if list.size() == 0:
    #         print(-1)
    #     list[0]
