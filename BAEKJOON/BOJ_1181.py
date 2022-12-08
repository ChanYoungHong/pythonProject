
n = int(input())
array = []

for i in range(n):
    word = input()
    array.append(word)

set_word = list(set(array))

sort_word = []
for i in set_word:
    sort_word.append((len(i), i))

# result = sorted(sort_word)
sort_word.sort()

for len_word, word in sort_word:
    print(word)