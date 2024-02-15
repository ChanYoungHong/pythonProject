import sys
from collections import deque

input = sys.stdin.readline
'''
1. 1번 카드가 제일 위에
2. N번 카드가 제일 아래인 상태에
1,000,000

'''
n = int(input())

# deque1 = deque()
queue = []
discard = []

for i in range(1, n+1):
    # print('i : ', i)
    queue.append(i)



for _ in range(1, n):


    # 1 빠지고
    discard.append(queue.pop(0))
    # 2가 젤 먼저인 상황
    queue.append(queue.pop(0))


discard.append(queue.pop(0))

print(*discard)