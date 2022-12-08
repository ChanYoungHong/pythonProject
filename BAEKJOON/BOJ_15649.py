#
# n, m = map(int, input().split())
# visited = [False] * n
# out = []

import sys

        # 0 , 3, 1
# def solve(d, n, m):
#     if d == m:
#         print(" ".join(map(str, result)))
#         return
#     for i in range(n): # i -> 0 1 2
#         if visited[i] == False:
#             visited[i] = True
#             result.append(i + 1)
#             solve(d + 1, n, m)
#             visited[i] = False # 이유 몰랐으나 다시 찾음, false를 해줘야 다시 담을 때 true, false를 확인 할 수 있음.
#             result.pop()
#
# n,m = map(int, input().split())
#
# visited = [False] * n
# result = []
# solve(0, n, m)




def solve(k,n,m):
    if k == m:
        print(" ".join(map(str, result)))
        return
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            result.append(i + 1)
            solve(k+1, n, m)
            visited[i] = False
            result.pop()


n, m = map(int, input().split())

visited = [False] * n
result = []
solve(0,n,m)

n, m = list(map(int, input().split()))
s = []
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        if i not in s:
            s.append(i)
            dfs(i + 1)
            s.pop()

dfs(1)
















#### 12월 6일 다시 풀어보기

n, m = map(int, input().split())

visited = [False] * n
result = []











