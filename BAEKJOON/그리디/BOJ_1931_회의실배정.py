'''
1. 시간복잡도 -
2. 아이디어 - 람다 사용을 할 줄 알아야 함
'''

import sys

input = sys.stdin.readline

n = int(input())
result = []

for i in range(n):
    a, b = map(int, input().split())
    result.append((a,b))

result = sorted(result, key=lambda x:x[0])
result = sorted(result, key=lambda x:x[1])

last = 0
cnt = 0
for i,j in result:
    if i >= last:
        last = j
        cnt += 1

print(cnt)
# for _ in range(n):
#     a, b = map(int, input().split())
#     result.append((a,b))
#
# result.sort()
#
# print(result)
# answer = []
# for i in range(n):
#     temp = abs(result[i][1] - result[i][0])
#     answer.append(temp)
#
# print(answer)

