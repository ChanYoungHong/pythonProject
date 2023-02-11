import sys

input = sys.stdin.readline

n, m = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

'''
이진탐색을 사용해서 인덱스의 위치를 출력하면 될 것 같다.
1. 오븐의 깊이가 같을 때 오른쪽 것을 먼저 선택하게 만들고
2. 그 인덱스의 위치값을 반환하면 될 듯.
'''

for i in range(n-1):

    if oven[i] < oven[i+1]:
        oven[i+1] = oven[i]

dep = 0
for i in range(n-1,-1,-1):

    if pizza[dep] <= oven[i]:
        dep += 1


    if dep == m:
        print(i+1)
        sys.exit()

print(0)


