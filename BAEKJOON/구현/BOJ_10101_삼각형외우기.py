import sys

input = sys.stdin.readline

arr = [int(input()) for _ in range(3)]


if sum(arr) == 180:
    if arr[0] == arr[1] == arr[2]:
        print('Equilateral')
    elif sum == 180 and arr[0] == arr[1] or arr[1] == arr[2] or arr[0] == arr[2]:
        print('Isosceles')
    elif sum == 180 and arr[0] != arr[1] or arr[1] != arr[2] or arr[0] != arr[2]:
        print('Scalene')
else:
    print('Error')
