'''


'''
import sys

input = sys.stdin.readline

n = int(input())

answer = 0
for i in range(n):
    word = input()
    check = 0

    for j in range(len(word) - 1):
        if word[j] != word[j + 1]:
            new_word = word[j + 1:]

            if new_word.count(word[j]) > 0:
                check += 1

    if check == 0:
        answer += 1

print(answer)
