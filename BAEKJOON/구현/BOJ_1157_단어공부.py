import sys

input = sys.stdin.readline

word = input().rstrip()
word = word.upper()

arr = list(set(word))

answer = []
for i in arr:
    answer.append(word.count(i))


if answer.count(max(answer)) > 1:
    print('?')
else:
    max_index = answer.index(max(answer))
    print(arr[max_index])