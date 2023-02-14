
import sys

input = sys.stdin.readline

word = input().rstrip()

result = set()
for i in range(len(word)):
    for j in range(i, len(word)):
        result.add(word[i:j+1])


print(len(result))
