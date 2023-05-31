import sys

input = sys.stdin.readline

n = int(input())

word = []
for i in range(n):
    word.append(input().rstrip())

result = list(set(word))

answer = []
for j in result:
    answer.append((len(j), j))



# print(word)
answer.sort()
# print(answer)

# answer = sorted(answer, lambda=key x:x[0])

for i,j in answer:
    print(j)