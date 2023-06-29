import sys

input = sys.stdin.readline

n = int(input())

# arr = [input().rstrip() for _ in range(n)]


ans = 0
for i in range(n):

    word = input().rstrip()
    cnt = 0

    for j in range(len(word) - 1):

        if word[j] != word[j+1]:
           new_word = word[j+1:]

           if new_word.count(word[j]) > 0:
               cnt += 1

    if cnt == 0:
        ans += 1

print(ans)
