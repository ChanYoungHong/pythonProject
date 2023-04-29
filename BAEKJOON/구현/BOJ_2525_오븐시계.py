import sys

input = sys.stdin.readline

'''
<포인트>

1. 훈제오리구이를 시작하는 시간 -> 분단위로 주어졌을 때.
2. 오브구이가 끝나는 시간을 계산해라


첫 -> 시와 분을 공백으로
둘 -> 요리를 하는데 필요한 시간
'''

a, b = map(int, input().split())
time = int(input())

sum = (a * 60) + b + time

h = (sum // 60)
m = (sum % 60)

if h == 24:
    h = 0
    print(h, m)
elif h > 24:
    print(h-24, m)
else:
    print(h, m)

# for i in range(24): # 0 ~ 23
#     for j in range(60): # 0 ~ 59

# while True:

# if b + time >= 60:
#     a += 1
#     print(a, b)
# elif b + time >= 120:
#     a += 2
#     print(a, b)
# else:
#     print(a, b+time)




