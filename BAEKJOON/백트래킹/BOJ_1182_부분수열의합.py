
import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n, m = map(int,input().split())
nums = list(map(int, input().split()))

result = []
cnt = 0
def dfs(start):

    global cnt

    if sum(result) == m and len(result) > 0:
        cnt += 1

    for i in range(start, n):
        result.append(nums[i])
        dfs(i+1)
        result.pop()

dfs(0)
print(cnt)



