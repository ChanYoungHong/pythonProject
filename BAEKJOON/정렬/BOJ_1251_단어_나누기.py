import sys

input = sys.stdin.readline

word = input().rstrip()
res = []
for i in range(1, len(word)):
    for j in range(i+1, len(word)):

        x = word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]
        res.append(x)


print(min(res))