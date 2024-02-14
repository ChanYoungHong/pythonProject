import sys

input = sys.stdin.readline

'''
1. 1, 3, 5, 7, 8, 10, 12월은 31일까지,
2. 4, 6, 9, 11월은 30일까지, 
3. 2월은 28일까지 있다.

'''

a = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

x,y = map(int, input().split())
day = 0

for i in range(0, x - 1):
    day += b[i]

result = (day + y) % 7

print(a[result])