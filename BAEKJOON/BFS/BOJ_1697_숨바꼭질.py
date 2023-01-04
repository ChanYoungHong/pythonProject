# from collections import deque
# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# cnt = 0
#
# oper = [-1,1,2]
#
# def bfs():
#
#     global cnt
#
#     q = deque()
#     q.append()
#
#     while q:
#         x,y = q.popleft()
#
#         for i in range(3):
#             if x == y:
#                 break
#
#             elif x < y:
#                 nx = x + oper[i]
#                 cnt += 1
#                 q.append(nx)
#                 if i == 2:
#                     nx = x * oper[i]
#                     cnt += 1
#                     q.append(nx)
#
# print(bfs())

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0

maxx = 10 ** 5
array = [0] * (maxx + 1)


def bfs():
    global cnt

    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == m:
            print(array[x])
            break

        for j in (x + 1, x - 1, x * 2):
            if 0 <= j <= maxx and not array[j]:
                array[j] = array[x] + 1
                q.append(j)


bfs()
