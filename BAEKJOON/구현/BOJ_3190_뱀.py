import sys
from collections import deque

input = sys.stdin.readline

'''
1. 사과를 먹으면 뱀의 길이가 늘어난다
2. 벽 또는 자기자신에게 부딪히면 게임 끝
3. 머리를 다음칸에 위치 
4. if 사과가 있다면, 사과가 없어지고 꼬리는 움직이지 않는다.
5. if 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

뱀의 몸의 길이를 어떻게 표현을 하나?
-> 
'''

n = int(input())

board = [[0] * n for _ in range(n)]
q = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]


for i in range(int(input())):

    a,b = map(int, input().split())
    q.append((a,b))


for j in range(int(input())):

    c,d = input().split()
    q.append((c,d))

while q:

    x,y = q.popleft()

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
