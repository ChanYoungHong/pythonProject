'''

1. 시간복잡도 -
2. 아이디어 - 백트래킹을 사용해야 함

'''

import sys

input = sys.stdin.readline


def dfs(dep, idx):
    if dep == 6:
        print(*result)

    for i in range(idx, k):
        result.append(nums[i])
        dfs(dep + 1, i + 1)
        result.pop()


while True:

    array = list(map(int, input().split()))
    k = array[0]
    nums = array[1:]
    result = []
    dfs(0, 0)

    if k == 0:
        exit()
    print()