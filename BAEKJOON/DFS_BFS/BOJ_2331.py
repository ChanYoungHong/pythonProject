import sys

input = sys.stdin.readline

A, p = map(int, input().split())
check = [0] * 200
cnt = 1


def cal(a, b):
    result = 0
    for i in str(a):
        result += pow(int(i), b)
    return result


def dfs(A, p, cnt, check):
    if check[A] != 0:
        return check[A] - 1

    check[A] = cnt
    cnt += 1
    result = cal(A, p)
    return dfs(result, p, cnt, check)


print(dfs(A, p, cnt, check))
