import sys

input = sys.stdin.readline

n = int(input())

arr = {}

for i in range(n):

    k,v = input().split()

    if v == 'enter':
        arr[k] = v
    else:
        del arr[k]

arr = sorted(arr.keys(), reverse = True)

for i in arr:
    print(i)

