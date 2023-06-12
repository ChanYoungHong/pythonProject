import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):

    tt = input().rstrip()

    cnt = 0
    for j in tt:

        if j == '(':
            cnt += 1
        elif j == ')':
            cnt -= 1

        if cnt > 0:
            print('NO')
            break

    if cnt < 0:
        print('NO')
    elif cnt == 0:
        print('YES')
