import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    word = input().rstrip()

    cnt = 0
    for i in word:

        if i == '(':
            cnt -= 1
        elif i == ')':
            cnt += 1

        if cnt > 0:
            print('NO')
            break

    if cnt <  0:
        print('NO')
    elif cnt == 0:
        print('YES')
