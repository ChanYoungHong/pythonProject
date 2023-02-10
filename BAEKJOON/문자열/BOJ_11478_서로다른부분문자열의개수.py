
import sys

input = sys.stdin.readline

word = input().rstrip()

res = set()

for i in range(len(word)):
    for j in range(i, len(word)):

        res.add(word[i:j+1])

print(len(res))