# from itertools import permutations
#
#
# n = int(input())
# nums = list(map(int, input().split()))
#
#
# res = 0
# for per in permutations(nums):
#     temp = 0
#     for i in range(n-1):
#         temp += abs(per[i] - per[i+1])
#     res = max(res, temp)
#
# print(res)


n = int(input())
list = list(map(int ,input().split()))

visited = [False]*n
answer = 0

def sol(li):
  global answer
  if len(li) == n:
    total = 0
    for i in range(n-1): # 0 1 2 3 4 5
      total += abs(li[i]- li[i+1])
    answer = max(answer, total)
    return

  for i in range(n):
    if not visited[i]:
      visited[i] = True
      li.append(list[i])
      sol(li)
      visited[i] = False
      li.pop()

sol([])
print(answer)