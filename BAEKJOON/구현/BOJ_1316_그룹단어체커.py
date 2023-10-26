import sys

input = sys.stdin.readline

n = int(input())
answer = 0

for _ in range(n):
    word = input().rstrip()

    cnt = 0
    for i in range(len(word)-1):

        if word[i] != word[i+1]:
            new_word = word[i+1:]

            if new_word.count(word[i]) > 0:
                cnt += 1

    if cnt == 0:
        answer += 1

print(answer)
