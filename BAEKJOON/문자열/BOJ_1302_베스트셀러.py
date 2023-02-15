# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# words = []
# for i in range(n):
#     a = input().rstrip()
#     words.append(a)
#
# maxx = max(words)
# cnt = words.count(maxx)
#
# res = []
# for j in words:
#
#     if words.count(j) >= cnt:
#         res.append(j)
#     else:
#         continue
#
# res.sort()
# print(res[0])

import sys

book = dict()
n = int(input())

input = sys.stdin.readline
for _ in range(n):

    name = input().rstrip()

    if name in book:
        book[name] += 1
    else:
        book[name] = 1

max = 0
sbook = dict(sorted(book.items()))
for i in sbook:
    if (sbook[i]) > max:
        max = sbook[i]
        maxi = i
print(maxi)



