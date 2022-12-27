import sys

input = sys.stdin.readline

def dfs(dep, idx):

    if dep == 6:
        print(*result)
        return

    for i in range(idx, k):
        result.append(s[i])
        dfs(dep + 1, i + 1)
        result.pop()

while True:

    array = list(map(int, input().split()))
    k = array[0]
    s = array[1:]
    result = []
    dfs(0,0)
    if k == 0:
        exit()
    print()
