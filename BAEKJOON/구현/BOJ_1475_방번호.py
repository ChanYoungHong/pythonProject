import sys

input = sys.stdin.readline

number = input().rstrip()

sett = [0] * 9


for i in number:

    idx = int(i)

    if idx == 9:
        idx = 6
    sett[idx] += 1


sett[6] = (sett[6] + 1) // 2
print(max(sett))
