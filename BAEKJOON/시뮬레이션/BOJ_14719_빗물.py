import sys
from collections import deque

input = sys.stdin.readline

'''
1. 시간복잡도 및 어떻게 풀어갈지 고민하기 ! n < 500 n3이 나옴
2. 빗물이 퍼지는 느낌으로 bfs로 접근해야 할 것 같음 - 내 상각
3.  물의 높이를 어떻게 측정해서 계산을 도출 할까 ?
4. 

'''

# # h 세로 w 가로
# h,w = map(int, input().split())
# world = list(map(int, input().split()))
#
# # visited = [[0] * w for _ in range(h)]
#
# ans = 0
# for i in range(1, w-1):
#     left_max = max(world[:i])
#     right_max = max(world[i+1:])
#
#     compare = min(left_max, right_max)
#
#     if world[i] < compare:
#         ans += compare - world[i]
#
# print(ans)

# print(visited)
#
# print(rains)
#
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]



# def bfs(x,y):
#
#     q = deque()

# for i in range(h):
#     for j in range(len(rains) -1, 0, -1):
#
#         if visited[rains[j]][i] == 0:
#             visited[j][i] = 1
#             print('visited[j][i] : ', visited[j][i])
#
#
# for k in range(h):
#     for z in range(w):
#
#         print(visited[k][z], end = ' ')
#     print()

    # while q:
    #
    #     x,y = q.popleft()
    #
    #     for i in range(4):
    #         nx = x + dx[i]
    #         ny = y + dy[i]
    #
    #         if 0 <= nx < h and 0 <= ny < w:
    #
    #
    # return

H, W = map(int, input().split())
blocks = [*map(int, input().split())]
result = 0  # 빗물의 고인 양

for i in range(1, W - 1):  # 맨 왼쪽과 맨 오른쪽은 고일 수 없다.

    left_max = max(blocks[:i])  # 왼쪽에서 제일 높은 블록
    print('blocks[:i] : ', blocks[:i])
    print('left max : ', max(blocks[:i]))

    right_max = max(blocks[i + 1:])  # 오른쪽에서 제일 높은 블록
    print('blocks[i+1:] : ', blocks[i+1:])
    print('right max : ', max(blocks[i+1:]))

    lower_one = min(left_max, right_max)  # 그중 가장 낮은 블록
    print('lower_ond : ', lower_one)

    if blocks[i] < lower_one:  # 현재 블록이 lower_one 블록 보다는 낮아야 빗물이 고인다.
        result += lower_one - blocks[i]

print(result)