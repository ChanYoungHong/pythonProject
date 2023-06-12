import sys

input = sys.stdin.readline

word = input().rstrip()

cnt = 0
# for i in range(len(word) - 1):

#     if word[i] != word[i + 1]:
#         cnt += 1
#
# print((cnt + 1) // 2)

prev = '?'

for i in word:
    if i != prev:
        prev = i
        cnt += 1

print(cnt//2)