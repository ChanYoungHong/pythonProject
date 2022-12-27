# 두 배열 중 하나는 계속 고정이 되어 있어야 함
# 그래서 한 배열만 dfs으로 계속 값의 교체가 이루어져야 함

n = int(input())

nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

maxx = -1e9
minn = 1e9


def dfs(dep, total, add, minus, multi, divide):
    global maxx, minn

    if dep == n:
        maxx = max(total, maxx)
        minn = min(total, minn)
        return

    if add:
        dfs(dep + 1, total + nums[dep], add - 1, minus, multi, divide)
    if minus:
        dfs(dep + 1, total - nums[dep], add, minus - 1, multi, divide)
    if multi:
        dfs(dep + 1, total * nums[dep], add, minus, multi - 1, divide)
    if divide:
        dfs(dep + 1, int(total / nums[dep]), add, minus, multi, divide - 1)


dfs(1, nums[0], oper[0], oper[1], oper[2], oper[3])
print(maxx)
print(minn)
