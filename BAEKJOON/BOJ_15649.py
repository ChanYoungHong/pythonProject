#
# n, m = map(int, input().split())
# visited = [False] * n
# out = []

import sys

        # 0 , 3, 1
def solve(d, n, m):
    if d == m:
        print(" ".join(map(str, result)))
        return
    for i in range(n): # i -> 0 1 2
        if visited[i] == False:
            visited[i] = True
            result.append(i + 1)
            solve(d + 1, n, m)
            visited[i] = False # 이유 몰랐으나 다시 찾음, false를 해줘야 다시 담을 때 true, false를 확인 할 수 있음.
            result.pop()

# n, m = map(int, sys.stdin.readline().split())
n,m = map(int, input().split())

visited = [False] * n
result = []
solve(0, n, m)


