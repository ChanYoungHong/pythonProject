n = int(input())

words = []

for i in range(n):
    words.append(input())

set_word = list(set(words))

sort_word = []

for i in set_word:
    sort_word.append((len(i), i))

sort_word.sort()

for len, i in sort_word:
    print(i)
