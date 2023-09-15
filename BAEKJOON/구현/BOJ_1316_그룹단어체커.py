import sys

input = sys.stdin.readline

n = int(input())

cnt = 0
for _ in range(n):

    word = input().rstrip()

    t = 0
    for i in range(len(word) - 1):

        if word[i] != word[i+1]:
            new_word = word[i+1:]

            if new_word.count(word[i]) > 0:
                t += 1

    if t == 0:
        cnt += 1

print(cnt)

