'''

1. 시간복잡도 - n < 1000아라 2중 for문을 사용해도 됨
2. 아이디어 - m으로 지정 된 나를 골라서 기준으로 만들어서 구분한다.

'''

import sys

input = sys.stdin.readline
n, m = map(int,input().split())

result = []

for i in range(n):
    ranking = list(map(int, input().split()))

    if ranking[0] != m:
        result.append(ranking)
    else:
        standard = ranking

'''
등수는 자신보다 더 잘한 나라 수 + 1
cnt = 1이 되어야한다.
'''

cnt = 1 # 등수
for i in range(len(result)):
    if result[i][1] > standard[1]:
        cnt += 1

    elif result[i][1] == standard[1]:
        if result[i][2] > standard[2]:
            cnt += 1

        elif result[i][2] == standard[2]:
            if result[i][3] > standard[3]:
                cnt += 1

print(cnt)