'''

n < 10,000 보다 작으니깐 투 포인터가 적합 함

'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

end = 0
temp_num = 0
cnt = 0

for i in range(n):

    while temp_num < m and end < n:
        temp_num += num[end]
        end += 1

    if temp_num == m:
        cnt += 1

    temp_num -= num[i]

print(cnt)
