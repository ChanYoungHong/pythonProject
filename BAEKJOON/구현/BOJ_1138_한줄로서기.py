import sys
from collections import deque, defaultdict

'''

수도코드 -> 
1. memory가 가장 큰 애는 항상 젤 왼쪽에 넣기
2. 


'''
input = sys.stdin.readline

# 처음 내 나름대로 구현한 방식

# n = int(input())
# memory = list(map(int, input().rstrip().split()))

#
#
# temp = []
# for i in range(n):
#     temp.append((i+1, memory[i]))
#
# temp = sorted(temp, key= lambda x:x[1])
#
# result = []
# for idx, memo in temp:
#
#     if memo == 0:
#         result.append(idx)
#     elif len(result) == memo:
#         result.append(idx)
#     elif idx not in result:
#         result.append(idx)
#
# print(result)
'''

아이디어 

1. 4번이 젤 크다, 4 > 2 > 1 > 3
2. 

'''

n = int(input())
memo = list(map(int, input().split()))

temp = [0] * n

for i in range(n):

    cnt = 0
    for j in range(n):

        if cnt == memo[i] and temp[j] == 0:
            temp[j] = i + 1

        elif temp[j] == 0:
            cnt += 1

print(temp)