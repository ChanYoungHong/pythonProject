import sys

input = sys.stdin.readline

n = int(input())

ans = ''
real = 0
cnt = 0
new_ans = 0

# while True:
#
#     if n < 10:
#         ans = '0' + str(n)
#         real = (int(ans) // 10) + (int(ans) % 10)
#         cnt += 1
#
#         if n == real:
#             print(cnt)
#             break
#
#     elif n >= 10:
#
#         tt = n
#
#         summ = (tt // 10) + (tt % 10)
#         # print(summ)
#         print('summ = ', summ)
#
#         if summ >= 10:
#
#             ss = (summ // 10) + (summ % 10)
#             n = a3
#         else:
#             a3 = str(tt % 10) + str(summ)
#             tt = a3
#
#
#     if tt

num = n

while True:

    a = num // 10
    # a = 2
    b = num % 10
    # b = 6
    c = (a+b) % 10
    # 8 % 10
    num = (b * 10) + c
    # 80 + 8

    cnt += 1
    if (num == n):
        break

print(cnt)
