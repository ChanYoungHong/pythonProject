n, m = map(int, input().split())

visited = [False] * (n + 1)
result = []

def rec(d):

    if d == m:
        print(' '.join(map(str, result)))
        return

    for i in range(1, n+1):
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            rec(d+1)
            visited[i] = False
            result.pop()

rec(0)
