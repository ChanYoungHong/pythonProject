N = int(input())
condition = list(map(int,input().split()))
visit = [False] * N
mx = 0
array = []
def DFS(v):
    global mx
    if v == N:
        now_sum = 0
        for i in range(N-1):
            now_sum += abs(array[i]-array[i+1])
        mx = max(now_sum, mx)
        return
    for i in range(N):
        if visit[i] == False:
            visit[i] = True
            array.append(condition[i])
            DFS(v+1)
            array1.pop()
            visit[i] = False

DFS(0)
print(mx)
