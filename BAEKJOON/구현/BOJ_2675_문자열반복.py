import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):

    num, word = input().split()
    answer = ''

    for i in word:
        answer += i*int(num)
    print(answer)