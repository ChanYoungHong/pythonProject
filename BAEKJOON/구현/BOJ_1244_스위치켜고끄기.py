import sys

input = sys.stdin.readline


n = int(input())
arr = [0] + list(map(int, input().split()))

student = int(input())

def change(x):

    arr[x] = abs(arr[x] - 1)

    return arr[x]

for _ in range(student):

    gender, button = map(int, input().split())
    i = 1

    if gender == 1:

        while button * i <= 8:
            change(button * i)
            i += 1

    elif gender == 2:

        change(button)
        while 1 <= button - i and button + i <= n and arr[button-i] == arr[button+i]:
            change(button + i)
            change(button - i)
            i += 1

for i in range(1, len(arr)):
    print(arr[i], end=' ')

    if not i % 20:
        print()