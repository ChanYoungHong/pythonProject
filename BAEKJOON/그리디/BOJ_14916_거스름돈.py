'''


'''

import sys

input = sys.stdin.readline

n = int(input())
import sys

input = sys.stdin.readline

n = int(input())

money = [2, 5]
cnt = 0

while True:

    if n % money[1] == 0:
        cnt += n // money[1]
        break
    elif n % money[0] == 0:
        n -= money[0]
        cnt += 1
    else:
        n -= money[1]
        cnt += 1

    if n < 0:
        break

if n < 0:
    print(-1)
else:
    print(cnt)
money = [2, 5]
cnt = 0

while True:

    if n % money[1] == 0:
        cnt += n // money[1]
        break
    elif n % money[0] == 0:
        n -= money[0]
        cnt += 1
    else:
        n -= money[1]
        cnt += 1

    if n < 0:
        break

if n < 0:
    print(-1)
else:
    print(cnt)
