import sys

input = sys.stdin.readline

'''
1. A가 n의 약수가 되려면
2. n이 a의 배수가 되고 
3. a가 1과 n이 아니어야 함



'''

# 진짜 약수의 개수
n = int(input())

real_num = list(map(int, input().split()))
# print(real_num)

real_num.sort()
# print(real_num)

a = real_num[0] * real_num[-1]
print(a)