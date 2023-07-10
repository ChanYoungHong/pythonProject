import sys

input = sys.stdin.readline



sett = [0] * 9

num = input().rstrip()

for i in num:

    idx = int(i)

    if idx == 9:
        idx = 6
    sett[idx] += 1

sett[6] = (sett[6] + 1) // 2

# print(sett[6])
print(max(sett))
