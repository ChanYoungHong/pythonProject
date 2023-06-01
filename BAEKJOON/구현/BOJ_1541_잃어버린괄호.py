import sys

input = sys.stdin.readline

text = input().rstrip().split('-')

res = []
for i in text:

    x = i.split('+')
    sum = 0

    for j in x:
        sum += int(j)
    res.append(sum)


b = res[0]

for i in range(1, len(res)):
    b -= res[i]

print(b)