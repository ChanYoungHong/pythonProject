import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    aa = list(input())
    total = 0
    summ = 0

    for i in aa:
        if i == 'O':
            summ += 1
            total += summ
        else:
            summ = 0
    print(total)


