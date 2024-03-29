import sys

input = sys.stdin.readline

n,m = map(int, input().split())
nums = list(map(int, input().split()))

test = []
def dfs(dep):

    if len(test) == m:
        print(*test)
        return

    nums.sort()

    # for i in nums:
    #     if i not in test:
    #         test.append(i)
    #         dfs(dep, i)
    #         test.pop()

    for i in range(dep, n):
        test.append(nums[i])
        dfs(i)
        test.pop()



dfs(0)