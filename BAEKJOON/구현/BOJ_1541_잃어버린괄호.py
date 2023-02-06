import sys

input = sys.stdin.readline

word = input().rstrip().split('-')

result = []
for i in word:

    sum = 0
    new_word = i.split('+')

    for j in new_word:

        sum += int(j)
    result.append(sum)

z = result[0]

for k in range(1, len(result)):
    z -= result[k]

print(z)
