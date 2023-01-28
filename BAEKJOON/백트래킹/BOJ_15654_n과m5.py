import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
result = []
def dfs(dep):

    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    nums.sort()

    for i in nums:
        if i not in result:
            result.append(i)
            dfs(dep+1)
            result.pop()

dfs(1)
