import sys

input = sys.stdin.readline


n = int(input())

cnt = 0
for _ in range(n):

    word = input().rstrip()
    arr = []

    for k in range(len(word)):

        if arr:

            if word[k] == arr[-1]:
                arr.pop()
            else:
                arr.append(word[k])
        else:
            arr.append(word[k])

    if not arr:
        cnt += 1

print(cnt)

print(cnt)