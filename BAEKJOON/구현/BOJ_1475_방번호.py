import sys

input = sys.stdin.readline

word = input().rstrip()
numSet = [0] * 9
for i in word:

    idx = int(i)

    if idx == 9:
        idx = 6
    numSet[idx] += 1

numSet[6] = (numSet[idx] + 1) // 2

print(max(numSet))
