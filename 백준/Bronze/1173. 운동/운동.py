import sys

input = sys.stdin.readline

'''
1. N분 운동 -> 5분 운동
2. N분 하려는데 필요한 시간의 최솟값
3. 맥박이 T만큼 증가한다 -> 25만큼
4. M이 넘는 것을 원하지 않음, m + T
5. N는 시간, 
m은 초기맥박, 
T씩 증가
M은 최대맥박량
R은 R씩 증가

'''
N, m, M, T, R = map(int, input().split())

X = m
total = minute = 0

if m + T > M:
    print(-1)

else:
    while minute < N:
        # 여기 조건에서만 운동을 할 수 있음
        if X+T <= M:
            # 운동을 할 때
            X = X + T
            minute += 1
            total += 1
        # 휴식할 때
        else:
            # 휴식을 할 때
            X = X - R
            # minute += 1

            if X < m:
                X = m
            total += 1

    print(total)