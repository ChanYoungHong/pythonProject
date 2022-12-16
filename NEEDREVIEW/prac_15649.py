n, m = map(int, input().split())
visited = [False] * (n + 1)
result = []


def recc(deph):

    if deph == m:
        print(' '.join(map(str, result)))
        return

    for i in range(1, n+1):
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            recc(deph + 1)
            visited[i] = False
            result.pop()

recc(0)
