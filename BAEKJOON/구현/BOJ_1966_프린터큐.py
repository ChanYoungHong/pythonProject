import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    idx = list(range(len(arr)))
    idx[m] = 'target'

    order = 0

    while True:

        if max(arr) == arr[0]:
            order += 1

            if idx[0] == 'target':
                print(order)
                break

            else:
                arr.pop(0)
                idx.pop(0)

        else:
            arr.append(arr.pop(0))
            idx.append(idx.pop(0))
