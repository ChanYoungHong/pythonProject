import sys

input = sys.stdin.readline
'''
N - 스크린
M - 바구니(왼쪽 오른쪽 이동이 가능하다)

'''

n, m = map(int, input().split())
apple = int(input())

left = 1
right = m
cnt = 0

for _ in range(apple):
    position = int(input())

    # 사과가 바구니에 안 떨어질 때
    if left <= position and right >= position:
        continue

    # 사과가 왼쪽에 가깝게 떨어질 때
    elif left > position:
        cnt += (left - position)
        right -= (left - position)
        left = position

    # 사과가 오른쪽에 가깝게 떨어질 때
    else:
        cnt += (position - right)
        left += (position - right)
        right = position

print(cnt)
