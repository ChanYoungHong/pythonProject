import sys

input = sys.stdin.readline

t = int(input())

'''

알게된 점 -> not visited 부분을 False로 바꿔서 답을 제출하면 
Recursion Error가 뜸 신기함 

'''

def dfs(num):

    visited[num] = True
    aa = arr[num]

    if not visited[aa]:
        dfs(aa)


for i in range(t):

    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [True] + [False] * n
    res = 0

    for j in range(1, n+1):

        if not visited[j]:
            dfs(j)
            res += 1

    print(res)


