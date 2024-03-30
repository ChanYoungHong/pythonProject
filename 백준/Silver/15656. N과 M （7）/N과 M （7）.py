import sys

input = sys.stdin.readline

n,m = map(int, input().split())
nums = list(map(int, input().split()))

test = []

def dfs():

    if len(test) == m:
        print(*test)
        return


    nums.sort()

    for i in nums:
        test.append(i)
        dfs()
        test.pop()

dfs()