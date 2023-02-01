
import sys

input = sys.stdin.readline

word = input().rstrip().split('-')

result = []
for i in word:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    result.append(cnt)

z = result[0]

for i in range(1, len(result)):
    z -= result[i]

print(z)







# word = list(input().rstrip())
# word = input().rstrip()
#
# print(word.split('+'))
#
# result = word.split('+')
#
# answer = list(map(int, result))
# print(sum(answer))

