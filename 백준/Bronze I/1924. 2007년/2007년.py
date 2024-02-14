import sys

input = sys.stdin.readline

'''
1. 1, 3, 5, 7, 8, 10, 12월은 31일까지,
2. 4, 6, 9, 11월은 30일까지, 
3. 2월은 28일까지 있다.

'''

days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
c = [2]


x,y = list(map(int, input().split()))


# 1 2 3
total = 0
rest = 0
for i in range(1, x+1):

    if i in a:
        # print('a+i : ', i)
        total += 31
        rest = 31 - y
    elif i in b:
        # print('b+i : ', i)
        total += 30
        rest = 30 - y
    else:
        # print('c+i : ', i)
        total += 28
        rest = 28 - y

    if x == i:
        if i in a:
            total = (total - rest)
        elif i in b:
            total = (total - rest)
        else:
            total = (total - rest)

print(days[total%7])