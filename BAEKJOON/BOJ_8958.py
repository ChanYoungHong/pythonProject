import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):

    a = list(input().rstrip())

    sum = 0
    total_sum = 0
    for i in range(len(a)):

        if a[i] == 'O':
            sum += 1
            total_sum += sum

        else:

            sum = 0

    print(total_sum)
