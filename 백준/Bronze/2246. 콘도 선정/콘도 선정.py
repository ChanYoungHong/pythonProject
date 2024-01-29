import sys

input = sys.stdin.readline


'''
1. 거리는 짧고, 가격

'''
n = int(input())

total_map = []
for _ in range(n):
    D,C = map(int, input().rstrip().split())
    total_map.append((D,C))

total_map.sort()
cost = 10001
result = 0

for i in total_map:

    temp = i[1]

    if temp < cost:
        cost = temp
        result += 1

print(result)