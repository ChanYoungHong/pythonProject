'''

1. 시간복잡도가 n < 300,000 밑으로니깐 nlogn을 써야해서 이진탐색을 사용해야한다

'''

import sys

input = sys.stdin.readline

d,n = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

for i in range(d-1):
    if oven[i] < oven[i+1]:
        oven[i+1] = oven[i]

cur = 0
for i in range(d-1, -1, -1):

    if pizza[cur] > oven[i]:
        continue

    cur += 1
    if cur >= n:
        print(i+1)
        sys.exit(0)

print(0)
