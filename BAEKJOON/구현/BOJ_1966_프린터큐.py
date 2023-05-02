import sys

input = sys.stdin.readline

# critical =

t = int(input())

ans = []
for _ in range(t):
    # m은 몇 번째 놓여 있는지 나타내는 정수
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
