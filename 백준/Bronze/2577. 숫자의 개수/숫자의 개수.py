import sys

input = sys.stdin.readline



check = '0123456789'

total = 1
for i in range(3):
    a = int(input())
    total *= a

for j in check:
    print(str(total).count(j))