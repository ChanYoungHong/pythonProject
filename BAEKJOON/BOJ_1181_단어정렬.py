import sys

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    word = input().rstrip()
    arr.append(word)

arrSet = list(set(arr))

answer = []
for a in arrSet:
    answer.append((len(a), a))

answer.sort()

for a,b in answer:
    print(b)