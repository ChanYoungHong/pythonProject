import sys

input = sys.stdin.readline

n = int(input())


dict = {'ChongChong'}

for _ in range(n):
    word1, word2 = input().rstrip().split()

    if word1 in dict:
        dict.add(word2)

    if word2 in dict:
        dict.add(word1)

print(len(dict))