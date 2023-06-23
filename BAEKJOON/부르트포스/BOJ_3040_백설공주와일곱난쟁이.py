import sys
from itertools import combinations

input = sys.stdin.readline

'''
포인트 ->

1. 의자 7 접시 7 나이프 7
2. 모자에 100보다 작은 양의 정수
3. 모자의 수의 합이 100이 되도록
4. 

'''

num = [int(input()) for _ in range(9)]

case = list(combinations(num, 7))

for i in case:
    if sum(i) == 100:
        for j in i:
            print(j)





