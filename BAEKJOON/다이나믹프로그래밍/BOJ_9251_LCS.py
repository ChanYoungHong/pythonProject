import sys

word1 = input()
word2 = input()

a, b = len(word1), len(word2)

array = [[0] * (b+1) for _ in range(a+1)]

for i in range(1, a+1):
    for j in range(1, b+1):
        if word1[i-1] == word2[j-1]:
            array[i][j] = array[i-1][j-1] + 1
        else:
            array[i][j] = max(array[i][j-1], array[i-1][j])

print(array[-1][-1])