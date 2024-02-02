import sys

input = sys.stdin.readline

'''
1. B는 버거개수, C는 사이드 메뉴 개수, D는 음료수 개수
2. 

'''

B, C, D = map(int, input().split())

burger = []
side = []
drink = []

burger = list(map(int, input().split()))
side= list(map(int, input().split()))
drink = list(map(int, input().split()))

burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)

total = 0
min_value = min(B,C,D)
for i in range(min_value):
    total += (burger[i] + side[i] + drink[i]) * 0.9

total += sum(burger[min_value::])
total += sum(side[min_value::])
total += sum(drink[min_value::])

print(sum(burger) + sum(side) + sum(drink))
print(int(total))
