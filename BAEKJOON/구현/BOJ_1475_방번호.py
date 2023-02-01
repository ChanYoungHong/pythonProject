import sys

input = sys.stdin.readline

n = input().rstrip()

p_set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cnt = 1

new_set = [0] * 10

for i in n:

    idx = int(i)

    if idx == 9:
        idx = 6

    new_set[idx] += 1
new_set[6] = (new_set[6] + 1) // 2
print(max(new_set))



