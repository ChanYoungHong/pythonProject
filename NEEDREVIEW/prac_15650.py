n, m = map(int, input().split())

result = []

def recursion(dep):

    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(dep, n + 1):
        if i not in result:
            result.append(i)
            recursion(i+1)
            result.pop()

recursion(1)

# def dfs(start):
#     if len(result) == m:
#         print(' '.join(map(str, result)))
#         return
#
#     for i in range(start, n+1):
#         if i not in result:
#             result.append(i)
#             dfs(i+1)
#             result.pop()
#
# dfs(1)