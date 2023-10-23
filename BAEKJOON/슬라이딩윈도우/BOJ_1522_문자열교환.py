import sys

input = sys.stdin.readline

word = list(input().rstrip())
a_cnt = word.count('a')
answer = 999999999999999
left = 0

while left < len(word):
    right = left + a_cnt

    if right > len(word):
        temp = word[left:len(word)] + word[:right - len(word)]
    else:
        temp = word[left:right]
    answer = min(answer, temp.count('b'))
    left += 1

print(answer)