
'''

1. 시간복잡도 -> 2 < n < 500 사이라서 n3 플로이드 워샬을 사용해야 함
2. 자산의 키가 몇 번째인지 알 수 있는 학생이 모두 몇 명인지 출력하기

# '''
#
# import sys
#
# INF = sys.maxsize
#
# input = sys.stdin.readline
#
# ''' n은 학생의 수, m은 두 학생 키를 비교한 횟수 '''
# n, m = map(int, input().split())
#
# graph = [[INF] * (n+1) for _ in range(n+1)]
#
# student = []
# for _ in range(n):
#     a, b = map(int, input().rstrip().split())
#     graph[a][b] = 1
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             graph[i][j] = 0
#
#
# for k in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if graph[i][j] == 1 or  (graph[i][k] == 1 or graph[k][j] == 1):
#                 graph[i][j] = 1
#
# answer = 0
# for i in range(1, n + 1):
#     known_height = 0
#     for j in range(1, n + 1):
#         known_height += graph[i][j] + graph[j][i]  # 자신보다 작은사람과 큰사람의 합
#     if known_height == n - 1:  # 자신의 키 순서를 알 경우
#         answer += 1
#
# print(answer)

import sys

#입력
N, M = map(int, input().split())
height = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    tall, short = map(int, sys.stdin.readline().split())
    height[tall][short] = 1

# for z in range(7):
#     print(height[z])
# print()

#플로이드 와샬 알고리즘
for k in range(1, N+1): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(1, N+1):
        for j in range(1, N+1): # 1 -> 3 -> 4 -> 2
            if height[i][j] == 1 or (height[i][k] ==1 and height[k][j] == 1):
                height[i][j] = 1 #자신보다 작은 경우


#출력
answer = 0
for i in range(1, N+1): # 1 2 3 4 5 6
    known_height = 0
    for j in range(1, N+1): # 1 2 3 4 5 6
        # 1 < 4 + 4 < 1 = 1
        # 2 < 4 + 4 < 2 = 1
        # 3 < 4 + 4 < 3 = 1
        # 5 < 4 + 5 < 4 = 1
        # 4 < 6 + 6 < 4 = 1
        known_height += height[i][j] + height[j][i] #자신보다 작은사람과 큰사람의 합
    if known_height == N-1: #자신의 키 순서를 알 경우
        answer += 1

print(answer)

