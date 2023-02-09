import sys

input = sys.stdin.readline

word = input().rstrip().split('-')

res = []
for i in word:

    new_word = i.split('+')
    sum = 0
    for j in new_word:
        sum += int(j)
    res.append(sum)

zz = res[0]

for k in range(1, len(res)):
    zz -= res[k]

print(zz)
