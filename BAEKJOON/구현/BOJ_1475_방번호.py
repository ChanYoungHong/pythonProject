import sys

input = sys.stdin.readline

word = input().rstrip()

array = [0] * 9

for i in word:
    idx = int(i)

    if idx == 9:
        idx = 6

    array[idx] += 1

array[6] = (array[6] + 1) // 2

print(max(array))
