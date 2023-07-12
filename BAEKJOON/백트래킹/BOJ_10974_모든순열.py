import sys

input = sys.stdin.readline

n = int(input())

arr = []

def dfs():

    if len(arr) == n:
        print(*arr)

    for i in range(1, 1+n):

        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()

dfs()

