import sys

input = sys.stdin.readline

n = int(input().rstrip())
array = []

for _ in range(n):
    array.append(input().rstrip())

result = list(set(array))

answer = []
for i in result:
    answer.append((len(i), i))

answer.sort()

for num,key in answer:
    print(key)