from collections import deque
#
#  <수도코드>
#
#
#
#
#
#
#
n,m = map(int, input().split())
array = []

# 추가
for i in range(n):
    array.append(list(map(int, input().split())))

# 좌우위아래 막혔나, 비었나 확인하기 위함
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# visited = [False] * 5 * 5 # 행, 열 5 x 5 같이 0으로 초기화를 해줘야
# for문을 2개 돌리는 것도 좋은 방법인 것 같음.

def solve(array,n,m): # 재귀로 풀 수 있을 것 같음
    # if d == m:
    #     print("개수")
    #     print("넓이")
    # return
    queue = deque()
    queue.append((n, m))
    array[n][m] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft() # 첫 번째 원소를 제거한다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if array[nx][ny] == 1:
                array[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt

paint = []
for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            paint.append(solve(array, i, j))


if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))



# 벽에 막혔을 때 적을 코드
# if "최종벽에 부딪힐 때, 또는 비어있지 않을 때 등등":
#     return "ddd"