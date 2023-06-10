import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())

for i in range(t):

    n = int(input())
    arr = []
    for j in range(n):
        a,b = input().split()
        arr.append(b)

    num = 1
    res = Counter(arr)

    for key in res:
        num *= res[key] + 1

    print(num - 1)
