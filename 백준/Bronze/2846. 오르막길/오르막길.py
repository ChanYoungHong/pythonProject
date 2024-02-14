import sys

input = sys.stdin.readline

'''
1. 적어도 2개의 수로 이루어진 높이가 증가하는 부분 수열이다.
2. 오르막의 크기는 마지막 - 첫 번째의 차이이다.
3.
4.

'''
n = int(input())
load = list(map(int, input().split()))


# 0 1 2 3
compare = []
tmp = 0
for i in range(len(load) - 1):

    if load[i] < load[i+1]:
       tmp += load[i+1] - load[i]
    else:
        compare.append(tmp)
        tmp = 0

compare.append(tmp)
print(max(compare))