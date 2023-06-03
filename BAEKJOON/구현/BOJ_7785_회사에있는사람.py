import sys

input = sys.stdin.readline

n = int(input())

temp = dict()

for i in range(n):

    k,v = input().split()

    if v == 'enter':
        temp[k] = v
    else:
        del temp[k]

temp = sorted(temp.keys(), reverse=True)

for i in temp:
    print(i)


# check = {}
# for i in range(n):
#     v, k = input().split()
#
#     if check.get(k) == None:
#         check[k] = set()
#     check[k].add(v)
#
# for k,v in check.items():
#     if k == 'leave':






