# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# nums = list(map(int, input().split()))
# visited = [False] * (n + 1)
# result = 0
# res = []
# Nsum = 0
#
#
# def dfs(dep):
#     global result
#
#     if dep == n:
#         Nsum = 0
#         for i in range(n - 1):
#             Nsum += abs(res[i] - res[i + 1])
#         result = max(result, Nsum)
#
#     for i in range(n):
#
#         if visited[i] == False:
#             visited[i] = True
#             res.append(nums[i])
#             dfs(dep + 1)
#             res.pop()
#             visited[i] = False
#
#
# dfs(0)
# print(result)


from itertools import permutations

n = int(input())
nums = list(map(int,input().split()))

ans = 0

for per in permutations(nums):
    res = 0
    for i in range(n-1):
        res += abs(per[i] - per[i+1])
        print(per[i], per[i+1])

    ans = max(ans, res)

print(ans)
