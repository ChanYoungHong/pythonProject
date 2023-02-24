import sys

input =sys.stdin.readline

word = input().rstrip()
num = [0] * 9

for i in word:

    idx = int(i)

    if idx == 9:
        idx = 6

    num[idx] += 1

num[6] = (num[6] + 1) // 2

print(max(num))