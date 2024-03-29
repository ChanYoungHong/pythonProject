import sys

input = sys.stdin.readline


n,m = map(int, input().split())
nums = list(map(int, input().split()))

temp = []
def dfs(idx):

    if len(temp) == m:
        print(*temp)
        return

    nums.sort()

    for i in range(idx, n):
        if nums[i] not in temp:
            temp.append(nums[i])
            dfs(i)
            temp.pop()


dfs(0)