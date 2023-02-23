import sys

input = sys.stdin.readline

N = int(input())

# arr = []
#
# for _ in range(n):
#     ex1, ex2, ex3 = map(str, input().split())
#     arr.append((ex1,ex2,ex3))

INF = sys.maxsize

alphabet = "abcdefghijklmnopqrstuvwxyz"
n = len(alphabet)

graph = [[INF] * n for _ in range(n)]

for _ in range(N):
    a, b = map(alphabet.index, input().rstrip().split(" is "))
    graph[a][b] = 1

'''a is b -> graph[0][1]'''
'''b is c -> graph[1][2]'''
'''c is d -> graph[2][3]'''

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

M = int(input())
for _ in range(M):
    a, b = map(alphabet.index, input().rstrip().split(" is "))
    if graph[a][b] == INF:
        print("F")
    else:
        print("T")



# # 플로이드 와샬 알고리즘
# for k in range(1, N + 1):  # 경로 for문이 가장 상위 단계여야 누락되지 않는다
#     for i in range(1, N + 1):
#         for j in range(1, N + 1):
#             if height[i][j] == 1 or (height[i][k] == 1 and height[k][j] == 1):
#                 height[i][j] = 1  # 자신보다 작은 경우