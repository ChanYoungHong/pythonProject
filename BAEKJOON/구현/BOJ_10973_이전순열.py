import sys

input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if a[i] < a[i-1]: # 1 < 2
        x, y = i-1, i # 4 5
        for j in range(N-1, 0, -1):
            if a[j] < a[x]: # a[5] < a[4]
                a[j], a[x] = a[x], a[j]
                a = a[:i] + sorted(a[i:], reverse=True)
                print(*a)
                exit(0)
print(-1)

# result = []
# answer = []
# def dfs():
#
#     if len(result) == n:
#         print(*result)
#         return
#
#     for i in range(1, n+1):
#         if i not in result:
#             result.append(i)
#             dfs()
#             result.pop()
#
# dfs()
