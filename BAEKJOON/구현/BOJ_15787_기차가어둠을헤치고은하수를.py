import sys

input = sys.stdin.readline

'''
1. 기차번호 1 ~ N번으로 매길 때, 
2. 명령 4가지가 있음 -> 
3. 1번 이미 사람이 탔다면 -> 아무런 행동을 하지 않음
4. 2번 X번째 앉은 사람은 하차함, 만약 아무도 그 자리에 앉지
았는다면 아무런 행동을 X
5. 
6. n 기차의 수, m 명령의 수 
7.

'''

n, m = map(int, input().split())
train = [[0 for _ in range(20)] for _ in range(n)]
state = []

# 주어진 명령의 수만큼 반복합니다.
for i in range(m):

    order = list(map(int, input().split()))


    # 해당 기차의 특정 좌석을 1로 설정
    if order[0] == 1:
        train[order[1] -1][order[2]-1] = 1

    # 특정 좌석을 0으로 설정
    elif order[0] == 2:
        train[order[1]-1][order[2]-1] = 0

    # 해당 기차의 좌석을 한 칸 오른쪽으로 이동시킴,
    # 마지막 좌석은 0으로 설정하기
    elif order[0] == 3:
        for i in range(19, 0, -1):
            train[order[1]-1][i] = train[order[1]-1][i-1]
        train[order[1]-1][0] = 0

    # 해당 기차의 좌석을 한 칸 왼쪽으로 이동시킵니다.
    # 첫 번째 좌석은 0으로 설정됩니다.

    elif order[0] == 4:
        for i in range(19):
            train[order[1]-1][i] = train[order[1]-1][i+1]
        train[order[1]-1][19] = 0

cnt = 0
for i in range(n):
    if train[i] not in state:
        state.append(train[i])
        cnt += 1

print(cnt)
